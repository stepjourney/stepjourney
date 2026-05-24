#!/usr/bin/env python3
"""
generate_spots.py
=================
stairs/index.html 内の spotsData を読み込んで stairs/spot/S*.html を一括生成するスクリプト。

使い方：
    1. このスクリプトを stepjourney/stairs/ フォルダに置く
    2. stairs/index.html を最新の状態にする（スポットの追加・編集・削除はここで行う）
    3. ターミナルで stairs/ フォルダに移動する
         cd path/to/stepjourney/stairs
    4. 実行する
         python3 generate_spots.py
    5. stairs/spot/ フォルダに S*.html が生成（上書き）される
    6. 生成された spot/ フォルダの中身を GitHub にアップロードする

index.html の spotsData を更新したら、このスクリプトを再実行してください。
"""

import json
import os
import re

# ── パス設定 ──────────────────────────────────────────────
INDEX_HTML = os.path.join(os.path.dirname(__file__), 'index.html')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'spot')
# ─────────────────────────────────────────────────────────

EXTS = ['jpg', 'JPG', 'png']

def load_spots(index_path):
    """index.html 内の spotsData を抽出してパースする"""
    with open(index_path, encoding='utf-8') as f:
        src = f.read()
    # コメント行を除去
    src = re.sub(r'//[^\n]*', '', src)
    # const spotsData = [...]; の [...] 部分を抽出
    m = re.search(r'const\s+spotsData\s*=\s*(\[[\s\S]+?\])\s*;', src)
    if not m:
        raise ValueError('index.html から spotsData が見つかりませんでした')
    return json.loads(m.group(1))

def fmt_steps(val):
    if isinstance(val, int):
        return f"{val:,}"
    return str(val)

def fmt_date(s):
    y, m, d = s.split('-')
    return f"{y}年{int(m)}月{int(d)}日"

def esc(s):
    return (str(s)
        .replace('&', '&amp;').replace('<', '&lt;')
        .replace('>', '&gt;').replace('"', '&quot;'))

def img_tag(base, alt, css_id=None, style='width:100%;height:100%;object-fit:cover;display:block;'):
    srcs = [f"../images/{base}.{e}" for e in EXTS]
    attrs = f'src="{srcs[0]}" data-fb1="{srcs[1]}" data-fb2="{srcs[2]}"'
    id_attr = f' id="{css_id}"' if css_id else ''
    return f'<img{id_attr} {attrs} alt="{esc(alt)}" style="{style}" onerror="imgFallback(this)">'

def photo_section(names, spot_name):
    if not names:
        return '<div class="photo-main"><div class="photo-placeholder">写真準備中</div></div>', ''
    main = f'<div class="photo-main">{img_tag(names[0], "メイン写真", "main-img")}</div>'
    if len(names) > 1:
        thumbs_inner = ''.join(
            f'<div class="photo-thumb{"  active" if i == 0 else ""}" data-target="main-img" data-base="{n}">'
            f'{img_tag(n, f"写真{i+1}")}</div>'
            for i, n in enumerate(names)
        )
        thumbs = f'<div class="photo-thumbs">{thumbs_inner}</div>'
    else:
        thumbs = ''
    return main, thumbs

def map_section(names, spot_name):
    if not names:
        return '<div class="map-placeholder">地図準備中</div>'
    main = f'<div class="map-img">{img_tag(names[0], "地図", "main-map", style="width:100%;display:block;")}</div>'
    if len(names) > 1:
        thumbs_inner = ''.join(
            f'<div class="map-thumb{"  active" if i == 0 else ""}" data-target="main-map" data-base="{n}">'
            f'{img_tag(n, f"地図{i+1}")}</div>'
            for i, n in enumerate(names)
        )
        main += f'<div class="map-thumbs">{thumbs_inner}</div>'
    return main

def access_html(access):
    if not access:
        return '<div class="station-item">情報なし</div>'
    return ''.join(
        f'<div class="station-item">'
        f'<span class="station-name">{esc("・".join(a["line"]))} {esc(a["station"])}</span>'
        f'<span class="station-access">徒歩{a["walk_minutes"]}分</span>'
        f'</div>'
        for a in access
    )

CSS = '''
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  :root {
    --ai:#1b3a6b; --ai-mid:#2d5a9e; --ai-light:#e8eef7;
    --stone-bg:#f7f5f0; --stone-bd:#ddd8d0; --gold:#b8962e;
    --text-dark:#1a1a2e; --text-mid:#4a4a6a; --text-mute:#8888aa; --white:#ffffff;
  }
  body { font-family:-apple-system,BlinkMacSystemFont,'Hiragino Kaku Gothic ProN','Noto Sans JP',sans-serif; background:var(--stone-bg); color:var(--text-dark); font-size:15px; line-height:1.6; max-width:480px; margin:0 auto; min-height:100vh; }
  header { background:var(--ai); padding:14px 16px 12px; display:flex; justify-content:space-between; align-items:center; position:sticky; top:0; z-index:100; }
  .logo { color:#fff; font-size:20px; font-weight:600; letter-spacing:0.04em; }
  .logo-en { color:rgba(255,255,255,0.5); font-size:10px; font-weight:400; letter-spacing:0.1em; margin-top:1px; }
  .logo-link { text-decoration:none; display:block; }
  header nav { display:flex; gap:12px; align-items:center; }
  header nav a { color:rgba(255,255,255,0.8); font-size:12px; text-decoration:none; }
  .lang-btn { font-size:11px; border:1px solid rgba(255,255,255,0.35); border-radius:5px; padding:3px 9px; color:rgba(255,255,255,0.8); background:transparent; cursor:pointer; }
  .breadcrumb { padding:10px 16px; font-size:12px; color:var(--text-mute); background:var(--stone-bg); border-bottom:1px solid var(--stone-bd); display:flex; gap:6px; flex-wrap:wrap; align-items:center; }
  .breadcrumb a { color:var(--text-mute); text-decoration:none; }
  .breadcrumb a:hover { color:var(--text-mid); }
  .breadcrumb-sep { color:#ccc; }
  .breadcrumb-current { color:var(--text-mid); }
  .spot-hdr { background:var(--ai); padding:22px 16px 20px; }
  .spot-hdr-name { color:#fff; font-size:20px; font-weight:700; line-height:1.4; margin-bottom:8px; }
  .spot-hdr-steps { color:#c8d8f0; font-size:40px; font-weight:700; display:flex; align-items:baseline; gap:4px; }
  .spot-hdr-unit { font-size:16px; color:rgba(255,255,255,0.45); font-weight:400; }
  .section-photos { margin:12px 12px 0; }
  .photo-main { background:var(--ai-mid); width:100%; max-height:260px; overflow:hidden; display:flex; align-items:center; justify-content:center; border-radius:13px 13px 0 0; border:1px solid var(--stone-bd); border-bottom:none; }
  .photo-main img { width:100%; height:100%; object-fit:cover; display:block; }
  .photo-placeholder { color:rgba(255,255,255,0.35); font-size:13px; padding:40px 0; }
  .photo-thumbs { display:flex; gap:6px; padding:8px 12px; background:#ede9e2; overflow-x:auto; border:1px solid var(--stone-bd); border-top:none; border-radius:0 0 13px 13px; }
  .photo-thumb { flex-shrink:0; width:72px; height:56px; border-radius:7px; overflow:hidden; background:#ccc; cursor:pointer; border:2px solid transparent; }
  .photo-thumb.active { border-color:var(--ai); }
  .photo-thumb img { width:100%; height:100%; object-fit:cover; display:block; }
  .map-img { width:100%; border-radius:8px; overflow:hidden; border:1px solid var(--stone-bd); display:block; }
  .map-img img { width:100%; display:block; object-fit:cover; }
  .map-thumbs { display:flex; gap:6px; margin-top:6px; overflow-x:auto; }
  .map-thumb { flex-shrink:0; width:72px; height:56px; border-radius:6px; overflow:hidden; background:#ccc; cursor:pointer; border:2px solid transparent; }
  .map-thumb.active { border-color:var(--ai); }
  .map-thumb img { width:100%; height:100%; object-fit:cover; display:block; }
  .map-placeholder { background:var(--stone-bg); border:1px dashed var(--stone-bd); border-radius:8px; padding:18px; text-align:center; font-size:12px; color:var(--text-mute); }
  .section { background:var(--white); margin:12px 12px 0; border-radius:13px; border:1px solid var(--stone-bd); padding:16px; }
  .section-ttl { font-size:12px; font-weight:600; color:var(--text-mid); letter-spacing:0.06em; margin-bottom:12px; border-left:3px solid var(--gold); padding-left:9px; }
  .info-row { display:flex; gap:12px; padding:10px 0; border-bottom:1px solid var(--stone-bd); font-size:14px; }
  .info-row:last-child { border-bottom:none; }
  .info-label { color:var(--text-mute); font-size:12px; min-width:76px; flex-shrink:0; padding-top:1px; }
  .info-value { color:var(--text-dark); flex:1; line-height:1.65; }
  .info-value a { color:var(--ai-mid); font-size:13px; word-break:break-all; }
  .station-item { margin-bottom:7px; }
  .station-item:last-child { margin-bottom:0; }
  .station-name { font-weight:600; display:block; }
  .station-access { font-size:12px; color:var(--text-mute); display:block; margin-top:1px; }
  .caution-box { background:var(--ai-light); border-left:3px solid var(--ai-mid); padding:11px 13px; font-size:13px; color:var(--text-mid); line-height:1.7; }
  .upd-row { display:flex; gap:10px; align-items:baseline; padding:8px 0; border-bottom:1px solid var(--stone-bd); font-size:13px; }
  .upd-row:last-child { border-bottom:none; }
  .upd-v { color:#ccc; min-width:26px; font-size:11px; }
  .upd-d { color:var(--text-mute); min-width:88px; font-size:12px; }
  .upd-n { color:var(--text-dark); }
  .back-btn { display:block; margin:14px 12px 24px; text-align:center; padding:12px; border:1px solid var(--stone-bd); border-radius:10px; font-size:14px; color:var(--text-mid); text-decoration:none; background:var(--white); cursor:pointer; }
  .back-btn:active { opacity:0.8; }
  footer { background:var(--ai); padding:18px 16px; text-align:center; font-size:11px; color:rgba(255,255,255,0.35); }
'''

JS = '''
  function imgFallback(img) {
    const tried = parseInt(img.dataset.tried || '0') + 1;
    img.dataset.tried = tried;
    const next = img.dataset['fb' + tried];
    if (next) { img.src = next; } else { img.style.display = 'none'; }
  }
  document.querySelectorAll('.photo-thumb, .map-thumb').forEach(thumb => {
    thumb.addEventListener('click', () => {
      const target = thumb.dataset.target;
      const group = thumb.classList.contains('photo-thumb') ? '.photo-thumb' : '.map-thumb';
      document.querySelectorAll(group).forEach(t => t.classList.remove('active'));
      thumb.classList.add('active');
      const img = document.getElementById(target);
      if (img) {
        const base = thumb.dataset.base;
        img.dataset.tried = '0';
        img.src = '../images/' + base + '.jpg';
        img.dataset.fb1 = '../images/' + base + '.JPG';
        img.dataset.fb2 = '../images/' + base + '.png';
      }
    });
  });
'''

GA4 = '''\
<script>
  if (localStorage.getItem('ga_exclude') !== 'true') {
    var script = document.createElement('script');
    script.async = true;
    script.src = 'https://www.googletagmanager.com/gtag/js?id=G-FC6FWPNHRK';
    document.head.appendChild(script);
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-FC6FWPNHRK');
  }
</script>'''

def generate_html(spot):
    sid   = spot['id']
    name  = spot['name']
    sv    = spot.get('steps', '')
    addr  = spot.get('address', '') or spot.get('prefecture', '')
    hist  = spot.get('history', [])
    caut  = spot.get('caution', '')
    ofurl = spot.get('official_url', '')

    photo_names = (spot.get('images') or {}).get('photos', [])
    map_names   = (spot.get('images') or {}).get('maps', [])

    # 段数
    if sv != '' and sv is not None:
        steps_text = fmt_steps(sv) + '段'
        steps_hdr  = f'<div class="spot-hdr-steps">{fmt_steps(sv)}<span class="spot-hdr-unit"> 段</span></div>'
    else:
        steps_text = '情報なし'
        steps_hdr  = ''

    addr_text = esc(addr) if addr else '情報なし'

    pm_html, th_html = photo_section(photo_names, name)
    mp_html  = map_section(map_names, name)
    ac_html  = access_html(spot.get('access', []))

    official_html = ''
    if ofurl:
        official_html = (
            f'<div class="info-row">'
            f'<div class="info-label">公式サイト</div>'
            f'<div class="info-value"><a href="{esc(ofurl)}" target="_blank" rel="noopener">{esc(ofurl)}</a></div>'
            f'</div>'
        )

    caution_html = ''
    if caut:
        caution_html = (
            f'<div class="section">'
            f'<div class="section-ttl">注意情報</div>'
            f'<div class="caution-box">{esc(caut)}</div>'
            f'</div>'
        )

    if hist:
        hist_html = ''.join(
            f'<div class="upd-row">'
            f'<div class="upd-v">v{h["version"]}</div>'
            f'<div class="upd-d">{fmt_date(h["date"])}</div>'
            f'<div class="upd-n">{esc(h["note"])}</div>'
            f'</div>'
            for h in hist
        )
    else:
        hist_html = '<div class="upd-row"><div class="upd-n">履歴なし</div></div>'

    ac_list  = spot.get('access', [])
    st_str   = '、'.join(f'{a["station"]}（徒歩{a["walk_minutes"]}分）' for a in ac_list)
    meta_desc = f'{name}（{steps_text}）の階段・石段スポット情報。'
    if st_str:
        meta_desc += f'最寄り駅：{st_str}。'
    meta_desc += '住所・写真・地図を掲載。'

    return f'''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(name)} - 段旅 StepJourney</title>
<meta name="description" content="{esc(meta_desc)}">
<link rel="canonical" href="https://stepjourney.github.io/stepjourney/stairs/spot/{sid}.html">
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(name)} - 段旅 StepJourney">
<meta property="og:description" content="{esc(meta_desc)}">
<meta property="og:url" content="https://stepjourney.github.io/stepjourney/stairs/spot/{sid}.html">
<meta property="og:image" content="https://stepjourney.github.io/stepjourney/stairs/images/{photo_names[0] if photo_names else sid + '-1'}.jpg">
<meta name="twitter:card" content="summary">
{GA4}
<style>{CSS}</style>
</head>
<body>

<header>
  <div>
    <a href="../index.html" class="logo-link">
      <div class="logo">段旅</div>
      <div class="logo-en">StepJourney</div>
    </a>
  </div>
  <nav>
    <a href="../../blog/index.html">階段・石段体験ブログ</a>
    <button class="lang-btn" onclick="alert('英語版は準備中です。')">EN</button>
  </nav>
</header>

<div class="breadcrumb">
  <a href="../index.html">段旅</a>
  <span class="breadcrumb-sep">&gt;</span>
  <span class="breadcrumb-current">{esc(name)}</span>
</div>

<div class="spot-hdr">
  <div class="spot-hdr-name">{esc(name)}</div>
  {steps_hdr}
</div>

<div class="section-photos">
  <div class="section-ttl" style="margin:12px 0 8px;border-left:3px solid var(--gold);padding-left:9px;font-size:12px;font-weight:600;color:var(--text-mid);">現地写真</div>
  {pm_html}
  {th_html}
</div>

<div class="section">
  <div class="section-ttl">階段・石段スポット基本情報</div>
  <div class="info-row">
    <div class="info-label">住所</div>
    <div class="info-value">{addr_text}</div>
  </div>
  <div class="info-row">
    <div class="info-label">地図</div>
    <div class="info-value">{mp_html}</div>
  </div>
  <div class="info-row">
    <div class="info-label">段数</div>
    <div class="info-value">{steps_text}</div>
  </div>
  <div class="info-row">
    <div class="info-label">最寄り駅</div>
    <div class="info-value">{ac_html}</div>
  </div>
  {official_html}
</div>

{caution_html}

<div class="section">
  <div class="section-ttl">更新履歴</div>
  {hist_html}
</div>

<a class="back-btn" href="../index.html">&#8592; スポット一覧に戻る</a>

<footer>&copy; 2026 段旅 StepJourney</footer>

<script>
{JS}
</script>
</body>
</html>'''


def main():
    print(f'index.html を読み込み中: {INDEX_HTML}')
    spots = load_spots(INDEX_HTML)
    print(f'  → {len(spots)} 件のスポットを読み込みました')

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    generated = []
    skipped   = []

    for spot in spots:
        sid = spot['id']
        if spot.get('disabled', 0) != 0:
            skipped.append(sid)
            continue
        html = generate_html(spot)
        out  = os.path.join(OUTPUT_DIR, f'{sid}.html')
        with open(out, 'w', encoding='utf-8') as f:
            f.write(html)
        generated.append(sid)
        print(f'  生成: {sid}.html')

    print(f'\n完了: {len(generated)} 件生成、{len(skipped)} 件スキップ（disabled）')
    if skipped:
        print(f'  スキップ: {", ".join(skipped)}')
    print(f'\n出力先: {OUTPUT_DIR}')


if __name__ == '__main__':
    main()

// =============================
// スポットデータ
// スポットを追加・編集する際はこのファイルを更新する
// =============================
const spotsData = [
  {
    "id": "S001",
    "disabled": 0,
    "name": "東京タワーの外階段",
    "steps": "600",
    "elevation_diff": "約150m",
    "address": "東京都港区芝公園4-2-8",
    "prefecture": "東京都",
    "access": [
      {
        "type": "train",
        "line": [
          "都営大江戸線"
        ],
        "station": "赤羽橋駅",
        "walk_minutes": 5
      }
    ],
    "caution": "",
    "images": {
      "photos": [
        "S001-1",
        "S001-2",
        "S001-3"
      ],
      "maps": [
        "S001-map1"
      ]
    },
    "history": [
      {
        "version": 1,
        "date": "2026-05-09",
        "note": "新規掲載"
      }
    ]
  },
  {
    "id": "S002",
    "disabled": 0,
    "name": "多摩川台公園の階段",
    "steps": "103",
    "elevation_diff": "約15m",
    "address": "東京都大田区田園調布1-57付近",
    "prefecture": "東京都",
    "access": [
      {
        "type": "train",
        "line": [
          "東急多摩川線"
        ],
        "station": "多摩川駅",
        "walk_minutes": 10
      }
    ],
    "caution": "",
    "images": {
      "photos": [
        "S002-1",
        "S002-2",
        "S002-3"
      ],
      "maps": [
        "S002-map1",
        "S002-map2"
      ]
    },
    "history": [
      {
        "version": 1,
        "date": "2026-05-09",
        "note": "新規掲載"
      }
    ]
  },
  {
    "id": "S003",
    "disabled": 0,
    "name": "亀塚公園の階段",
    "steps": "136",
    "elevation_diff": "約19m",
    "address": "東京都港区三田4-17-20",
    "prefecture": "東京都",
    "access": [
      {
        "type": "train",
        "line": [
          "都営浅草線"
        ],
        "station": "泉岳寺駅",
        "walk_minutes": 15
      }
    ],
    "caution": "",
    "images": {
      "photos": [
        "S003-1",
        "S003-2",
        "S003-3"
      ],
      "maps": [
        "S003-map1"
      ]
    },
    "history": [
      {
        "version": 1,
        "date": "2026-05-09",
        "note": "新規掲載"
      }
    ]
  },
  {
    "id": "S004",
    "disabled": 0,
    "name": "愛宕神社の出世の石段",
    "steps": 86,
    "elevation_diff": "約17m",
    "address": "東京都港区愛宕1-5-3",
    "prefecture": "東京都",
    "access": [
      {
        "type": "train",
        "line": [
          "東京メトロ日比谷線"
        ],
        "station": "神谷町駅",
        "walk_minutes": 5
      }
    ],
    "caution": "",
    "images": {
      "photos": [
        "S004-1",
        "S004-2",
        "S004-3"
      ],
      "maps": [
        "S004-map1"
      ]
    },
    "history": [
      {
        "version": 1,
        "date": "2026-05-09",
        "note": "新規掲載"
      }
    ]
  },
  {
    "id": "S005",
    "disabled": 0,
    "name": "玉川病院そばの階段",
    "steps": "130",
    "elevation_diff": "",
    "address": "東京都世田谷区岡本2-24付近",
    "prefecture": "東京都",
    "access": [
      {
        "type": "train",
        "line": [
          "東急田園都市線"
        ],
        "station": "二子玉川駅",
        "walk_minutes": 20
      }
    ],
    "caution": "",
    "images": {
      "photos": [
        "S005-1",
        "S005-2",
        "S005-3"
      ],
      "maps": [
        "S005-map1",
        "S005-map2"
      ]
    },
    "history": [
      {
        "version": 1,
        "date": "2026-05-09",
        "note": "新規掲載"
      }
    ]
  },
  {
    "id": "S006",
    "disabled": 0,
    "name": "薬王院そばの階段",
    "steps": "71",
    "elevation_diff": "",
    "address": "東京都新宿区下落合4-8",
    "prefecture": "東京都",
    "access": [
      {
        "type": "train",
        "line": [
          "西武新宿線"
        ],
        "station": "下落合駅",
        "walk_minutes": 10
      }
    ],
    "caution": "",
    "images": {
      "photos": [
        "S006-1",
        "S006-2",
        "S006-3"
      ],
      "maps": [
        "S006-map1",
        "S006-map2"
      ]
    },
    "history": [
      {
        "version": 1,
        "date": "2026-05-09",
        "note": "新規掲載"
      }
    ]
  },
  {
    "id": "S007",
    "disabled": 0,
    "name": "片倉城跡公園の階段",
    "steps": "68",
    "elevation_diff": "",
    "address": "",
    "prefecture": "東京都",
    "access": [
      {
        "type": "train",
        "line": [
          "京王線"
        ],
        "station": "京王片倉駅",
        "walk_minutes": 6
      }
    ],
    "caution": "",
    "images": {
      "photos": [
        "S007-1",
        "S007-2",
        "S007-3"
      ],
      "maps": [
        "S007-map1"
      ]
    },
    "history": [
      {
        "version": 1,
        "date": "2026-05-09",
        "note": "新規掲載"
      }
    ]
  },
  {
    "id": "S008",
    "disabled": 0,
    "name": "聖蹟桜ヶ丘のいろは坂の階段その1",
    "steps": "92",
    "elevation_diff": "",
    "address": "東京都多摩市桜ケ丘4付近",
    "prefecture": "東京都",
    "access": [
      {
        "type": "train",
        "line": [
          "京王線"
        ],
        "station": "聖蹟桜ヶ丘駅",
        "walk_minutes": 10
      }
    ],
    "caution": "",
    "images": {
      "photos": [
        "S008-1",
        "S008-2",
        "S008-3"
      ],
      "maps": [
        "S008-map1"
      ]
    },
    "history": [
      {
        "version": 1,
        "date": "2026-05-10",
        "note": "新規掲載"
      }
    ]
  },
  {
    "id": "S009",
    "disabled": 0,
    "name": "聖蹟桜ヶ丘のいろは坂の階段その2",
    "steps": "85",
    "elevation_diff": "",
    "address": "東京都多摩市桜ケ丘4付近",
    "prefecture": "東京都",
    "access": [
      {
        "type": "train",
        "line": [
          "京王線"
        ],
        "station": "聖蹟桜ヶ丘駅",
        "walk_minutes": 10
      }
    ],
    "caution": "",
    "images": {
      "photos": [
        "S009-1",
        "S009-2",
        "S009-3"
      ],
      "maps": [
        "S009-map1"
      ]
    },
    "history": [
      {
        "version": 1,
        "date": "2026-05-10",
        "note": "新規掲載"
      }
    ]
  },
  {
    "id": "S010",
    "disabled": 0,
    "name": "聖蹟桜ヶ丘のいろは坂の階段その3",
    "steps": "67",
    "elevation_diff": "",
    "address": "東京都多摩市桜ケ丘4付近",
    "prefecture": "東京都",
    "access": [
      {
        "type": "train",
        "line": [
          "京王線"
        ],
        "station": "聖蹟桜ヶ丘駅",
        "walk_minutes": 10
      }
    ],
    "caution": "",
    "images": {
      "photos": [
        "S010-1",
        "S010-2",
        "S010-3"
      ],
      "maps": [
        "S010-map1"
      ]
    },
    "history": [
      {
        "version": 1,
        "date": "2026-05-10",
        "note": "新規掲載"
      }
    ]
  },
  {
    "id": "S011",
    "disabled": 0,
    "name": "聖蹟桜ヶ丘のいろは坂の階段その4",
    "steps": "59",
    "elevation_diff": "",
    "address": "東京都多摩市桜ケ丘4付近",
    "prefecture": "東京都",
    "access": [
      {
        "type": "train",
        "line": [
          "京王線"
        ],
        "station": "聖蹟桜ヶ丘駅",
        "walk_minutes": 10
      }
    ],
    "caution": "",
    "images": {
      "photos": [
        "S011-1",
        "S011-2",
        "S011-3"
      ],
      "maps": [
        "S011-map1"
      ]
    },
    "history": [
      {
        "version": 1,
        "date": "2026-05-10",
        "note": "新規掲載"
      }
    ]
  },
  {
    "id": "S012",
    "disabled": 0,
    "name": "巨人への道",
    "steps": 283,
    "elevation_diff": "約45m",
    "address": "東京都稲城市矢野口4019",
    "prefecture": "東京都",
    "access": [
      {
        "type": "train",
        "line": [
          "京王相模原線"
        ],
        "station": "京王よみうりランド駅",
        "walk_minutes": 5
      }
    ],
    "caution": "",
    "images": {
      "photos": [
        "S012-1",
        "S012-2",
        "S012-3",
        "S012-4",
        "S012-5",
        "S012-6",
        "S012-7"
      ],
      "maps": [
        "S012-map1",
        "S012-map2"
      ]
    },
    "history": [
      {
        "version": 1,
        "date": "2026-05-12",
        "note": "新規掲載"
      }
    ]
  },
  {
    "id": "S013",
    "disabled": 0,
    "name": "日枝神社の階段その1",
    "steps": 132,
    "elevation_diff": "",
    "address": "東京都千代田区永田町2-10-5",
    "prefecture": "東京都",
    "access": [
      {
        "type": "train",
        "line": [
          "東京メトロ銀座線"
        ],
        "station": "赤坂見附駅",
        "walk_minutes": 10
      }
    ],
    "caution": "",
    "images": {
      "photos": [
        "S013-1",
        "S013-2",
        "S013-3"
      ],
      "maps": [
        "S013-map1"
      ]
    },
    "history": [
      {
        "version": 1,
        "date": "2026-05-09",
        "note": "新規掲載"
      }
    ]
  },
  {
    "id": "S014",
    "disabled": 0,
    "name": "日枝神社の階段その2",
    "steps": 63,
    "elevation_diff": "",
    "address": "東京都千代田区永田町2-10-5",
    "prefecture": "東京都",
    "access": [
      {
        "type": "train",
        "line": [
          "東京メトロ銀座線"
        ],
        "station": "赤坂見附駅",
        "walk_minutes": 10
      }
    ],
    "caution": "",
    "images": {
      "photos": [
        "S014-1",
        "S014-2",
        "S014-3"
      ],
      "maps": [
        "S014-map1",
        "S014-map2"
      ]
    },
    "history": [
      {
        "version": 1,
        "date": "2026-05-09",
        "note": "新規掲載"
      }
    ]
  },
  {
    "id": "S015",
    "disabled": 0,
    "name": "日枝神社の階段その3",
    "steps": 52,
    "elevation_diff": "",
    "address": "東京都千代田区永田町2-10-5",
    "prefecture": "東京都",
    "access": [
      {
        "type": "train",
        "line": [
          "東京メトロ銀座線"
        ],
        "station": "赤坂見附駅",
        "walk_minutes": 10
      }
    ],
    "caution": "",
    "images": {
      "photos": [
        "S015-1",
        "S015-2",
        "S015-3"
      ],
      "maps": [
        "S015-map1"
      ]
    },
    "history": [
      {
        "version": 1,
        "date": "2026-05-09",
        "note": "新規掲載"
      }
    ]
  },
  {
    "id": "S016",
    "disabled": 0,
    "name": "池上本門寺の階段その1(此経難持坂)",
    "steps": 96,
    "elevation_diff": "",
    "address": "東京都大田区池上1-1-1",
    "prefecture": "東京都",
    "access": [
      {
        "type": "train",
        "line": [
          "東急池上線"
        ],
        "station": "池上駅",
        "walk_minutes": 10
      }
    ],
    "caution": "",
    "images": {
      "photos": [
        "S016-1",
        "S016-2",
        "S016-3",
        "S016-4"
      ],
      "maps": [
        "S016-map1",
        "S016-map2"
      ]
    },
    "history": [
      {
        "version": 1,
        "date": "2026-05-09",
        "note": "新規掲載"
      }
    ]
  },
  {
    "id": "S017",
    "disabled": 0,
    "name": "池上本門寺の階段その2",
    "steps": 78,
    "elevation_diff": "",
    "address": "東京都大田区池上1-1-1",
    "prefecture": "東京都",
    "access": [
      {
        "type": "train",
        "line": [
          "東急池上線"
        ],
        "station": "池上駅",
        "walk_minutes": 10
      }
    ],
    "caution": "",
    "images": {
      "photos": [
        "S017-1",
        "S017-2",
        "S017-3",
        "S017-4"
      ],
      "maps": [
        "S017-map1",
        "S017-map2"
      ]
    },
    "history": [
      {
        "version": 1,
        "date": "2026-05-09",
        "note": "新規掲載"
      }
    ]
  },
  {
    "id": "S018",
    "disabled": 0,
    "name": "森浅間神社の階段その1",
    "steps": 244,
    "elevation_diff": "",
    "address": "神奈川県横浜市磯子区森2-16-7",
    "prefecture": "神奈川県",
    "access": [
      {
        "type": "train",
        "line": [
          "JR京浜東北線"
        ],
        "station": "磯子駅",
        "walk_minutes": 15
      }
    ],
    "caution": "",
    "images": {
      "photos": [
        "S018-1",
        "S018-2",
        "S018-3",
        "S018-4"
      ],
      "maps": [
        "S018-map1",
        "S018-map2"
      ]
    },
    "history": [
      {
        "version": 1,
        "date": "2026-05-18",
        "note": "新規掲載"
      }
    ]
  },
  {
    "id": "S019",
    "disabled": 0,
    "name": "森浅間神社の階段その2",
    "steps": 321,
    "elevation_diff": "",
    "address": "神奈川県横浜市磯子区森2-16-7",
    "prefecture": "神奈川県",
    "access": [
      {
        "type": "train",
        "line": [
          "JR京浜東北線"
        ],
        "station": "磯子駅",
        "walk_minutes": 10
      }
    ],
    "caution": "",
    "images": {
      "photos": [
        "S019-1",
        "S019-2",
        "S019-3"
      ],
      "maps": [
        "S019-map1",
        "S019-map2"
      ]
    },
    "history": [
      {
        "version": 1,
        "date": "2026-05-18",
        "note": "新規掲載"
      }
    ]
  }
];

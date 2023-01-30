from looqbox.render.looqbox.base_looqbox_render import BrowserRender
from looqbox.objects.api import *
import plotly.graph_objs as go
import pandas as pd
import unittest
import json


class TestLooqboxRender(unittest.TestCase):

    def setUp(self):

        self.render = BrowserRender()
        self.render.remove_nones = False

        self.message = ObjMessage("test message")
        self.html = ObjHTML("<div>Test HTML</div>")
        self.list = ObjList(["Item1", "Item2"])
        self.simple = ObjSimple("test simple")
        self.table = ObjTable()

        self.data = pd.DataFrame({"A": [1, 2], "B": [3, 4]})

    def test_message_render(self):

        model_json = json.loads("""{
        "objectType": "message",
        "text": [
         "test message"
        ],
        "type": "alert-default",
        "style": {
         "text-align": [
          "center"
          ]
         },
         "tabLabel": null
         }
         """)
        test_json = self.render.message_render(self.message)
        self.assertEqual(model_json, test_json)

    def test_html_render(self):

        model_json = json.loads("""
        {
         "objectType": "html",
         "html": "<div>Test HTML</div>",
         "tabLabel": null
         }""")

        test_json = self.render.html_render(self.html)
        self.assertEqual(model_json, test_json)

    # def test_list_render(self):
    #
    #     model_json = json.loads("""
    #     {
    #      "objectType": "list",
    #      "title": [],
    #      "list": [
    #       "Item1",
    #       "Item2"
    #       ],
    #       "type": "list",
    #       "placeholder": "Escolha uma das opções abaixo:"}""")
    #
    #     test_json = json.loads(self.render.obj_list_render(self.list))
    #
    #     self.assertEqual(model_json, test_json)
    #

    def test_simple_render(self):

        model_json = json.loads("""
         {
          "objectType": "simple",
          "text": "test simple"
          }""")

        test_json = self.render.simple_render(self.simple)

        self.assertEqual(model_json, test_json)

#     def test_table_render(self):
#
#         model_json = json.loads("""
#         {
#     "objectType": "table",
#     "title": [
#         null
#     ],
#     "header": {
#         "visible": true,
#         "_lq_cell_config": {
#             "A": {
#                 "class": [
#                     "lqDefault"
#                 ]
#             },
#             "B": {
#                 "class": [
#                     "lqDefault"
#                 ]
#             }
#         },
#         "content": [
#             {
#                 "title": "A",
#                 "dataIndex": "A"
#             },
#             {
#                 "title": "B",
#                 "dataIndex": "B"
#             }
#         ]
#     },
#     "body": {
#         "_lq_column_config": {
#             "A": {
#                 "class": [
#                     "lqDefault"
#                 ]
#             },
#             "B": {
#                 "class": [
#                     "lqDefault"
#                 ]
#             }
#         },
#         "content": [
#             {
#                 "A": 1,
#                 "B": 3
#             },
#             {
#                 "A": 2,
#                 "B": 4
#             }
#         ]
#     },
#     "footer": {},
#     "drill": {},
#     "searchable": false,
#     "pagination": {
#         "active": false,
#         "config": {
#             "defaultPageSize": 0,
#             "hideOnSinglePage": true,
#             "pageSizeOptions": [
#                 "10",
#                 "20",
#                 "25",
#                 "50",
#                 "100"
#             ]
#         }
#     },
#     "framed": false,
#     "stacked": true,
#     "showBorder": true,
#     "showOptionBar": true,
#     "showHighlight": true,
#     "striped": true,
#     "sortable": true,
#     "scroll": {
#         "mobile": {
#             "horizontal": {
#                 "active": false,
#                 "scrollableAreaWidth": 3000
#             },
#             "vertical": {
#                 "active": false,
#                 "fixedFooter": false,
#                 "fixedHeader": false
#             }
#         },
#         "desktop": {
#             "horizontal": {
#                 "active": false,
#                 "scrollableAreaWidth": 3000
#             },
#             "vertical": {
#                 "active": false,
#                 "fixedFooter": false,
#                 "fixedHeader": false
#             }
#         }
#     }
# }""")
#
#         self.table.data = pd.DataFrame(self.data)
#
#         self.render.remove_nones = False
#         test_json = self.render.table_render(self.table)
#         # self.render.remove_nones = False
#
#         self.assertEqual(model_json, test_json)

#     def test_plotly_render(self):
#
#         #TODO fix json reading
#         plotly_string = """
#         {
#     "objectType": 'plotly',
#     "data": '[ {  'x': [   1,   2  ],  'y': [   3,   4  ],  'type': 'scatter' }]',
#     'layout': '{ 'title': {  'text': 'title' }, 'yaxis': {  'title': {   'text': 'test'  } }, 'template': {  'data': {   'histogram2dcontour': [    {     'type': 'histogram2dcontour',     'colorbar': {      'outlinewidth': 0,      'ticks': ''     },     'colorscale': [      [       0.0,       '#0d0887'      ],      [       0.1111111111111111,       '#46039f'      ],      [       0.2222222222222222,       '#7201a8'      ],      [       0.3333333333333333,       '#9c179e'      ],      [       0.4444444444444444,       '#bd3786'      ],      [       0.5555555555555556,       '#d8576b'      ],      [       0.6666666666666666,       '#ed7953'      ],      [       0.7777777777777778,       '#fb9f3a'      ],      [       0.8888888888888888,       '#fdca26'      ],      [       1.0,       '#f0f921'      ]     ]    }   ],   'choropleth': [    {     'type': 'choropleth',     'colorbar': {      'outlinewidth': 0,      'ticks': ''     }    }   ],   'histogram2d': [    {     'type': 'histogram2d',     'colorbar': {      'outlinewidth': 0,      'ticks': ''     },     'colorscale': [      [       0.0,       '#0d0887'      ],      [       0.1111111111111111,       '#46039f'      ],      [       0.2222222222222222,       '#7201a8'      ],      [       0.3333333333333333,       '#9c179e'      ],      [       0.4444444444444444,       '#bd3786'      ],      [       0.5555555555555556,       '#d8576b'      ],      [       0.6666666666666666,       '#ed7953'      ],      [       0.7777777777777778,       '#fb9f3a'      ],      [       0.8888888888888888,       '#fdca26'      ],      [       1.0,       '#f0f921'      ]     ]    }   ],   'heatmap': [    {     'type': 'heatmap',     'colorbar': {      'outlinewidth': 0,      'ticks': ''     },     'colorscale': [      [       0.0,       '#0d0887'      ],      [       0.1111111111111111,       '#46039f'      ],      [       0.2222222222222222,       '#7201a8'      ],      [       0.3333333333333333,       '#9c179e'      ],      [       0.4444444444444444,       '#bd3786'      ],      [       0.5555555555555556,       '#d8576b'      ],      [       0.6666666666666666,       '#ed7953'      ],      [       0.7777777777777778,       '#fb9f3a'      ],      [       0.8888888888888888,       '#fdca26'      ],      [       1.0,       '#f0f921'      ]     ]    }   ],   'heatmapgl': [    {     'type': 'heatmapgl',     'colorbar': {      'outlinewidth': 0,      'ticks': ''     },     'colorscale': [      [       0.0,       '#0d0887'      ],      [       0.1111111111111111,       '#46039f'      ],      [       0.2222222222222222,       '#7201a8'      ],      [       0.3333333333333333,       '#9c179e'      ],      [       0.4444444444444444,       '#bd3786'      ],      [       0.5555555555555556,       '#d8576b'      ],      [       0.6666666666666666,       '#ed7953'      ],      [       0.7777777777777778,       '#fb9f3a'      ],      [       0.8888888888888888,       '#fdca26'      ],      [       1.0,       '#f0f921'      ]     ]    }   ],   'contourcarpet': [    {     'type': 'contourcarpet',     'colorbar': {      'outlinewidth': 0,      'ticks': ''     }    }   ],   'contour': [    {     'type': 'contour',     'colorbar': {      'outlinewidth': 0,      'ticks': ''     },     'colorscale': [      [       0.0,       '#0d0887'      ],      [       0.1111111111111111,       '#46039f'      ],      [       0.2222222222222222,       '#7201a8'      ],      [       0.3333333333333333,       '#9c179e'      ],      [       0.4444444444444444,       '#bd3786'      ],      [       0.5555555555555556,       '#d8576b'      ],      [       0.6666666666666666,       '#ed7953'      ],      [       0.7777777777777778,       '#fb9f3a'      ],      [       0.8888888888888888,       '#fdca26'      ],      [       1.0,       '#f0f921'      ]     ]    }   ],   'surface': [    {     'type': 'surface',     'colorbar': {      'outlinewidth': 0,      'ticks': ''     },     'colorscale': [      [       0.0,       '#0d0887'      ],      [       0.1111111111111111,       '#46039f'      ],      [       0.2222222222222222,       '#7201a8'      ],      [       0.3333333333333333,       '#9c179e'      ],      [       0.4444444444444444,       '#bd3786'      ],      [       0.5555555555555556,       '#d8576b'      ],      [       0.6666666666666666,       '#ed7953'      ],      [       0.7777777777777778,       '#fb9f3a'      ],      [       0.8888888888888888,       '#fdca26'      ],      [       1.0,       '#f0f921'      ]     ]    }   ],   'mesh3d': [    {     'type': 'mesh3d',     'colorbar': {      'outlinewidth': 0,      'ticks': ''     }    }   ],   'scatter': [    {     'fillpattern': {      'fillmode': 'overlay',      'size': 10,      'solidity': 0.2     },     'type': 'scatter'    }   ],   'parcoords': [    {     'type': 'parcoords',     'line': {      'colorbar': {       'outlinewidth': 0,       'ticks': ''      }     }    }   ],   'scatterpolargl': [    {     'type': 'scatterpolargl',     'marker': {      'colorbar': {       'outlinewidth': 0,       'ticks': ''      }     }    }   ],   'bar': [    {     'error_x': {      'color': '#2a3f5f'     },     'error_y': {      'color': '#2a3f5f'     },     'marker': {      'line': {       'color': '#E5ECF6',       'width': 0.5      },      'pattern': {       'fillmode': 'overlay',       'size': 10,       'solidity': 0.2      }     },     'type': 'bar'    }   ],   'scattergeo': [    {     'type': 'scattergeo',     'marker': {      'colorbar': {       'outlinewidth': 0,       'ticks': ''      }     }    }   ],   'scatterpolar': [    {     'type': 'scatterpolar',     'marker': {      'colorbar': {       'outlinewidth': 0,       'ticks': ''      }     }    }   ],   'histogram': [    {     'marker': {      'pattern': {       'fillmode': 'overlay',       'size': 10,       'solidity': 0.2      }     },     'type': 'histogram'    }   ],   'scattergl': [    {     'type': 'scattergl',     'marker': {      'colorbar': {       'outlinewidth': 0,       'ticks': ''      }     }    }   ],   'scatter3d': [    {     'type': 'scatter3d',     'line': {      'colorbar': {       'outlinewidth': 0,       'ticks': ''      }     },     'marker': {      'colorbar': {       'outlinewidth': 0,       'ticks': ''      }     }    }   ],   'scattermapbox': [    {     'type': 'scattermapbox',     'marker': {      'colorbar': {       'outlinewidth': 0,       'ticks': ''      }     }    }   ],   'scatterternary': [    {     'type': 'scatterternary',     'marker': {      'colorbar': {       'outlinewidth': 0,       'ticks': ''      }     }    }   ],   'scattercarpet': [    {     'type': 'scattercarpet',     'marker': {      'colorbar': {       'outlinewidth': 0,       'ticks': ''      }     }    }   ],   'carpet': [    {     'aaxis': {      'endlinecolor': '#2a3f5f',      'gridcolor': 'white',      'linecolor': 'white',      'minorgridcolor': 'white',      'startlinecolor': '#2a3f5f'     },     'baxis': {      'endlinecolor': '#2a3f5f',      'gridcolor': 'white',      'linecolor': 'white',      'minorgridcolor': 'white',      'startlinecolor': '#2a3f5f'     },     'type': 'carpet'    }   ],   'table': [    {     'cells': {      'fill': {       'color': '#EBF0F8'      },      'line': {       'color': 'white'      }     },     'header': {      'fill': {       'color': '#C8D4E3'      },      'line': {       'color': 'white'      }     },     'type': 'table'    }   ],   'barpolar': [    {     'marker': {      'line': {       'color': '#E5ECF6',       'width': 0.5      },      'pattern': {       'fillmode': 'overlay',       'size': 10,       'solidity': 0.2      }     },     'type': 'barpolar'    }   ],   'pie': [    {     'automargin': true,     'type': 'pie'    }   ]  },  'layout': {   'autotypenumbers': 'strict',   'colorway': [    '#636efa',    '#EF553B',    '#00cc96',    '#ab63fa',    '#FFA15A',    '#19d3f3',    '#FF6692',    '#B6E880',    '#FF97FF',    '#FECB52'   ],   'font': {    'color': '#2a3f5f'   },   'hovermode': 'closest',   'hoverlabel': {    'align': 'left'   },   'paper_bgcolor': 'white',   'plot_bgcolor': '#E5ECF6',   'polar': {    'bgcolor': '#E5ECF6',    'angularaxis': {     'gridcolor': 'white',     'linecolor': 'white',     'ticks': ''    },    'radialaxis': {     'gridcolor': 'white',     'linecolor': 'white',     'ticks': ''    }   },   'ternary': {    'bgcolor': '#E5ECF6',    'aaxis': {     'gridcolor': 'white',     'linecolor': 'white',     'ticks': ''    },    'baxis': {     'gridcolor': 'white',     'linecolor': 'white',     'ticks': ''    },    'caxis': {     'gridcolor': 'white',     'linecolor': 'white',     'ticks': ''    }   },   'coloraxis': {    'colorbar': {     'outlinewidth': 0,     'ticks': ''    }   },   'colorscale': {    'sequential': [     [      0.0,      '#0d0887'     ],     [      0.1111111111111111,      '#46039f'     ],     [      0.2222222222222222,      '#7201a8'     ],     [      0.3333333333333333,      '#9c179e'     ],     [      0.4444444444444444,      '#bd3786'     ],     [      0.5555555555555556,      '#d8576b'     ],     [      0.6666666666666666,      '#ed7953'     ],     [      0.7777777777777778,      '#fb9f3a'     ],     [      0.8888888888888888,      '#fdca26'     ],     [      1.0,      '#f0f921'     ]    ],    'sequentialminus': [     [      0.0,      '#0d0887'     ],     [      0.1111111111111111,      '#46039f'     ],     [      0.2222222222222222,      '#7201a8'     ],     [      0.3333333333333333,      '#9c179e'     ],     [      0.4444444444444444,      '#bd3786'     ],     [      0.5555555555555556,      '#d8576b'     ],     [      0.6666666666666666,      '#ed7953'     ],     [      0.7777777777777778,      '#fb9f3a'     ],     [      0.8888888888888888,      '#fdca26'     ],     [      1.0,      '#f0f921'     ]    ],    'diverging': [     [      0,      '#8e0152'     ],     [      0.1,      '#c51b7d'     ],     [      0.2,      '#de77ae'     ],     [      0.3,      '#f1b6da'     ],     [      0.4,      '#fde0ef'     ],     [      0.5,      '#f7f7f7'     ],     [      0.6,      '#e6f5d0'     ],     [      0.7,      '#b8e186'     ],     [      0.8,      '#7fbc41'     ],     [      0.9,      '#4d9221'     ],     [      1,      '#276419'     ]    ]   },   'xaxis': {    'gridcolor': 'white',    'linecolor': 'white',    'ticks': '',    'title': {     'standoff': 15    },    'zerolinecolor': 'white',    'automargin': true,    'zerolinewidth': 2   },   'yaxis': {    'gridcolor': 'white',    'linecolor': 'white',    'ticks': '',    'title': {     'standoff': 15    },    'zerolinecolor': 'white',    'automargin': true,    'zerolinewidth': 2   },   'scene': {    'xaxis': {     'backgroundcolor': '#E5ECF6',     'gridcolor': 'white',     'linecolor': 'white',     'showbackground': true,     'ticks': '',     'zerolinecolor': 'white',     'gridwidth': 2    },    'yaxis': {     'backgroundcolor': '#E5ECF6',     'gridcolor': 'white',     'linecolor': 'white',     'showbackground': true,     'ticks': '',     'zerolinecolor': 'white',     'gridwidth': 2    },    'zaxis': {     'backgroundcolor': '#E5ECF6',     'gridcolor': 'white',     'linecolor': 'white',     'showbackground': true,     'ticks': '',     'zerolinecolor': 'white',     'gridwidth': 2    }   },   'shapedefaults': {    'line': {     'color': '#2a3f5f'    }   },   'annotationdefaults': {    'arrowcolor': '#2a3f5f',    'arrowhead': 0,    'arrowwidth': 1   },   'geo': {    'bgcolor': 'white',    'landcolor': '#E5ECF6',    'subunitcolor': 'white',    'showland': true,    'showlakes': true,    'lakecolor': 'white'   },   'title': {    'x': 0.05   },   'mapbox': {    'style': 'light'   }  } }}',
#     'stacked': true,
#     'displayModeBar': true,
#     'tabLabel': null
# }
#         """
#         model_json = json.loads(plotly_string)
#
#         trace = go.Scatter(x=list(self.data['A']), y=list(self.data['B']))
#         layout = go.Layout(title='title', yaxis=dict(title='test'))
#         self.plotly = ObjPlotly([trace], layout=layout)
#
#         test_json = json.loads(self.render.obj_plotly_render(self.plotly))
#
#         self.assertEqual(model_json, test_json)


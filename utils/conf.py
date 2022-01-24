hierarchical_food_web_visual_settings_inline = """
var options = {
  "edges": {
    "arrows": {
      "middle": {
        "enabled": true,
        "scaleFactor": 0.85
      },
    "smooth": {
        "enabled": true,
        "type": "continuous",
        "roundness": 0.1
      }
    },
    "color": {
      "inherit": true
    }
  },
  "layout": {
    "hierarchical": {
      "enabled": true,
      "nodeSpacing": 200
    }
  },
  "interaction": {
    "hover": true,
    "navigationButtons": false,
    "multiselect": true
  },
  "manipulation": {
    "enabled": false,
    "initiallyActive": false
  },
  "physics": {
    "enabled": true,
    "hierarchicalRepulsion": {
      "centralGravity": 0,
      "nodeDistance": 190
    },
    "minVelocity": 0.75,
    "solver": "hierarchicalRepulsion"
  },
  "configure": {
    "enabled": false
  }
}
"""

hierarchical_food_web_visual_settings_standalone = """
var options = {
  "edges": {
    "arrows": {
      "middle": {
        "enabled": true,
        "scaleFactor": 0.85
      }
    },
    "color": {
      "inherit": true
    },
    "smooth": false
  },
  "layout": {
    "hierarchical": {
      "enabled": true,
      "nodeSpacing": 200
    }
  },
  "interaction": {
    "hover": true,
    "navigationButtons": false,
    "multiselect": true
  },
  "manipulation": {
    "enabled": true,
    "initiallyActive": true
  },
  "physics": {
    "enabled": true,
    "hierarchicalRepulsion": {
      "centralGravity": 0,
      "nodeDistance": 190
    },
    "minVelocity": 0.75,
    "solver": "hierarchicalRepulsion"
  },
  "configure": {
    "enabled": true
  }
}
"""


my_style = {'description_width': 'initial'}
my_layout = {'width': 'max-content'}
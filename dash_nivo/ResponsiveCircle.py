# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ResponsiveCircle(Component):
    """A ResponsiveCircle component.


Keyword arguments:

- id (string; optional)

- borderColor (dict; default {    from: 'color',    modifiers: [['darker', 0.5]]})

- borderWidth (number; default 1)

- childColor (dict; default {    from: 'color',    // eslint-disable-next-line no-magic-numbers    modifiers: [['brighter', 0.4]]})

- colors (dict; default { scheme: 'nivo' })

- data (dict; required)

- defs (list; default [{    id: 'lines',    type: 'patternLines',    background: 'none',    color: 'inherit',    rotation: -45,    lineWidth: 5,    spacing: 8}])

- enableLabels (boolean; default True)

- fill (list; default [{    match: { depth: 1 },    id: 'lines'}])

- labelTextColor (dict; default {    from: 'color',    modifiers: [['darker', 2]]})

- labelsSkipRadius (number; default 16)

- margin (dict; default { top: 20, right: 20, bottom: 20, left: 20 })

- motionConfig (string; default 'slow')

- padding (number; default 4)

- zoomedId (string; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_nivo'
    _type = 'ResponsiveCircle'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, data=Component.REQUIRED, margin=Component.UNDEFINED, colors=Component.UNDEFINED, childColor=Component.UNDEFINED, padding=Component.UNDEFINED, enableLabels=Component.UNDEFINED, labelsFilter=Component.UNDEFINED, labelsSkipRadius=Component.UNDEFINED, labelTextColor=Component.UNDEFINED, borderWidth=Component.UNDEFINED, borderColor=Component.UNDEFINED, defs=Component.UNDEFINED, fill=Component.UNDEFINED, motionConfig=Component.UNDEFINED, zoomedId=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'borderColor', 'borderWidth', 'childColor', 'colors', 'data', 'defs', 'enableLabels', 'fill', 'labelTextColor', 'labelsSkipRadius', 'margin', 'motionConfig', 'padding', 'zoomedId']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'borderColor', 'borderWidth', 'childColor', 'colors', 'data', 'defs', 'enableLabels', 'fill', 'labelTextColor', 'labelsSkipRadius', 'margin', 'motionConfig', 'padding', 'zoomedId']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['data']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(ResponsiveCircle, self).__init__(**args)

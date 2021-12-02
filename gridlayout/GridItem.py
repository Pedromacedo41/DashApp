# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class GridItem(Component):
    """A GridItem component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Dash-assigned callback that should be called to report property
    changes to Dash, to make them available for callbacks.

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- h (number; optional)

- i (string; optional)

- maxH (number; optional)

- maxW (number; optional)

- minH (number; optional)

- minW (number; optional)

- w (number; optional)

- x (number; optional)

- y (number; optional)"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, i=Component.UNDEFINED, x=Component.UNDEFINED, y=Component.UNDEFINED, w=Component.UNDEFINED, h=Component.UNDEFINED, minW=Component.UNDEFINED, maxW=Component.UNDEFINED, minH=Component.UNDEFINED, maxH=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'h', 'i', 'maxH', 'maxW', 'minH', 'minW', 'w', 'x', 'y']
        self._type = 'GridItem'
        self._namespace = 'gridlayout'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'h', 'i', 'maxH', 'maxW', 'minH', 'minW', 'w', 'x', 'y']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(GridItem, self).__init__(children=children, **args)

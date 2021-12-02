# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class GridLayout(Component):
    """A GridLayout component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- layout (list; optional):
    Dash-assigned callback that should be called to report property
    changes to Dash, to make them available for callbacks."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, layout=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'layout']
        self._type = 'GridLayout'
        self._namespace = 'gridlayout'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'layout']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(GridLayout, self).__init__(children=children, **args)

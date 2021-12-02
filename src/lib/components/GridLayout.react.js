import React, {Component} from 'react';
import PropTypes from 'prop-types';
import RGL, {WidthProvider} from 'react-grid-layout';
import '../../../node_modules/react-grid-layout/css/styles.css';
import '../../../node_modules/react-resizable/css/styles.css';

const ResponsiveGridLayout = WidthProvider(RGL);

export default class GridLayout extends Component {

    /*constructor(props) {
        super(props);
        console.log("my children1: "+props.children);
    }*/

    render() {
        const {id, children, layout} = this.props;

        return (
            <ResponsiveGridLayout rowHeight={60} isBounded={true} compactType= {null} resizeHandles={["se", "s", "e"]}>
                {layout.map((item, index) => (
                    <div key={item.i} data-grid={item}>
                        {children[index]}
                    </div>
                ))} 
            </ResponsiveGridLayout>
        );
    }
}

GridLayout.defaultProps = {};

GridLayout.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    layout: PropTypes.array,
    children: PropTypes.node
};
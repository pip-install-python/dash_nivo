import React, { useState } from 'react';
import PropTypes from 'prop-types';
import { ResponsiveCirclePacking } from '@nivo/circle-packing';

const ResponsiveCircle = (props) => {
    const { id, data, margin, colors, childColor, padding, enableLabels, labelsFilter,
            labelsSkipRadius, labelTextColor, borderWidth, borderColor, defs, fill,
            motionConfig, setProps } = props;

    const [zoomedId, setZoomedId] = useState(null);

    const handleClick = (node) => {
        const newZoomedId = zoomedId === node.id ? null : node.id;
        setZoomedId(newZoomedId);
        if (setProps) {
            setProps({ zoomedId: newZoomedId });
        }
    };

    return (
        <div id={id} style={{ height: '400px' }}>
            <ResponsiveCirclePacking
                data={data}
                margin={margin}
                id="name"
                value="loc"
                colors={colors}
                childColor={childColor}
                padding={padding}
                enableLabels={enableLabels}
                labelsFilter={labelsFilter}
                labelsSkipRadius={labelsSkipRadius}
                labelTextColor={labelTextColor}
                borderWidth={borderWidth}
                borderColor={borderColor}
                defs={defs}
                fill={fill}
                zoomedId={zoomedId}
                motionConfig={motionConfig}
                onClick={handleClick}
            />
        </div>
    );
}

ResponsiveCircle.defaultProps = {
    margin: { top: 20, right: 20, bottom: 20, left: 20 },
    colors: { scheme: 'nivo' },
    childColor: {
        from: 'color',
        // eslint-disable-next-line no-magic-numbers
        modifiers: [['brighter', 0.4]]
    },
    padding: 4,
    enableLabels: true,
    labelsFilter: label => label.node.height === 0,
    labelsSkipRadius: 16,
    labelTextColor: {
        from: 'color',
        modifiers: [['darker', 2]]
    },
    borderWidth: 1,
    borderColor: {
        from: 'color',
        modifiers: [['darker', 0.5]]
    },
    defs: [{
        id: 'lines',
        type: 'patternLines',
        background: 'none',
        color: 'inherit',
        rotation: -45,
        lineWidth: 5,
        spacing: 8
    }],
    fill: [{
        match: { depth: 1 },
        id: 'lines'
    }],
    motionConfig: 'slow'
};

ResponsiveCircle._prop_names = [
    'id',
    'data',
    'margin',
    'colors',
    'childColor',
    'padding',
    'enableLabels',
    'labelsFilter',
    'labelsSkipRadius',
    'labelTextColor',
    'borderWidth',
    'borderColor',
    'defs',
    'fill',
    'motionConfig',
    'zoomedId',
]

ResponsiveCircle._type = 'DashNivo'

ResponsiveCircle._namespace = 'dash_nivo'

ResponsiveCircle._valid_wildcard_attributes = []

ResponsiveCircle.propTypes = {
    'id': PropTypes.string,
    'data': PropTypes.object.isRequired,
    'margin': PropTypes.object,
    'colors': PropTypes.object,
    'childColor': PropTypes.object,
    'padding': PropTypes.number,
    'enableLabels': PropTypes.bool,
    'labelsFilter': PropTypes.func,
    'labelsSkipRadius': PropTypes.number,
    'labelTextColor': PropTypes.object,
    'borderWidth': PropTypes.number,
    'borderColor': PropTypes.object,
    'defs': PropTypes.array,
    'fill': PropTypes.array,
    'motionConfig': PropTypes.string,
    'zoomedId': PropTypes.string,
}
export default ResponsiveCircle;
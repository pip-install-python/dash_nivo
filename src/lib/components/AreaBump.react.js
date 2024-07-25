import React from 'react';
import PropTypes from 'prop-types';
import { ResponsiveAreaBump } from '@nivo/bump';

const AreaBump = (props) => {
    const {
        id,
        data,
        margin,
        spacing,
        colors,
        blendMode,
        defs,
        fill,
        startLabel,
        endLabel,
        axisTop,
        axisBottom,
        setProps,
        clickedPoint
    } = props;

    return (
        <div id={id} style={{ height: '400px' }}>
            <ResponsiveAreaBump
                data={data}
                margin={margin}
                spacing={spacing}
                colors={colors}
                blendMode={blendMode}
                defs={defs}
                fill={fill}
                startLabel={startLabel}
                endLabel={endLabel}
                axisTop={axisTop}
                axisBottom={axisBottom}
                onClick={(point) => {
                    if (setProps) {
                        setProps({ clickedPoint: point });
                    }
                }}
            />
        </div>
    );
};

AreaBump.defaultProps = {
    margin: { top: 40, right: 100, bottom: 40, left: 100 },
    spacing: 8,
    colors: { scheme: 'nivo' },
    blendMode: 'multiply',
    defs: [
        {
            id: 'dots',
            type: 'patternDots',
            background: 'inherit',
            color: '#38bcb2',
            size: 4,
            padding: 1,
            stagger: true
        },
        {
            id: 'lines',
            type: 'patternLines',
            background: 'inherit',
            color: '#eed312',
            rotation: -45,
            lineWidth: 6,
            spacing: 10
        }
    ],
    fill: [
        {
            match: {
                id: 'CoffeeScript'
            },
            id: 'dots'
        },
        {
            match: {
                id: 'TypeScript'
            },
            id: 'lines'
        }
    ],
    startLabel: 'id',
    endLabel: 'id',
    axisTop: {
        tickSize: 5,
        tickPadding: 5,
        tickRotation: 0,
        legend: '',
        legendPosition: 'middle',
        legendOffset: -36,
        truncateTickAt: 0
    },
    axisBottom: {
        tickSize: 5,
        tickPadding: 5,
        tickRotation: 0,
        legend: '',
        legendPosition: 'middle',
        legendOffset: 32,
        truncateTickAt: 0
    },
    clickedPoint: null
};

AreaBump.propTypes = {
    id: PropTypes.string,
    data: PropTypes.array.isRequired,
    margin: PropTypes.object,
    spacing: PropTypes.number,
    colors: PropTypes.oneOfType([PropTypes.object, PropTypes.func]),
    blendMode: PropTypes.string,
    defs: PropTypes.array,
    fill: PropTypes.array,
    startLabel: PropTypes.oneOfType([PropTypes.string, PropTypes.func]),
    endLabel: PropTypes.oneOfType([PropTypes.string, PropTypes.func]),
    axisTop: PropTypes.object,
    axisBottom: PropTypes.object,
    setProps: PropTypes.func,
    clickedPoint: PropTypes.object
};

AreaBump._prop_names = [
    'id',
    'data',
    'margin',
    'spacing',
    'colors',
    'blendMode',
    'defs',
    'fill',
    'startLabel',
    'endLabel',
    'axisTop',
    'axisBottom',
    'clickedPoint'
];

AreaBump._type = 'AreaBump';

AreaBump._namespace = 'dash_nivo';

AreaBump._valid_wildcard_attributes = [];

export default AreaBump;
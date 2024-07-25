# AUTO GENERATED FILE - DO NOT EDIT

#' @export
dashNivo <- function(id=NULL, borderColor=NULL, borderWidth=NULL, childColor=NULL, colors=NULL, data=NULL, defs=NULL, enableLabels=NULL, fill=NULL, labelTextColor=NULL, labelsFilter=NULL, labelsSkipRadius=NULL, margin=NULL, motionConfig=NULL, padding=NULL, zoomedId=NULL) {
    
    props <- list(id=id, borderColor=borderColor, borderWidth=borderWidth, childColor=childColor, colors=colors, data=data, defs=defs, enableLabels=enableLabels, fill=fill, labelTextColor=labelTextColor, labelsFilter=labelsFilter, labelsSkipRadius=labelsSkipRadius, margin=margin, motionConfig=motionConfig, padding=padding, zoomedId=zoomedId)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashNivo',
        namespace = 'dash_nivo',
        propNames = c('id', 'borderColor', 'borderWidth', 'childColor', 'colors', 'data', 'defs', 'enableLabels', 'fill', 'labelTextColor', 'labelsFilter', 'labelsSkipRadius', 'margin', 'motionConfig', 'padding', 'zoomedId'),
        package = 'dashNivo'
        )

    structure(component, class = c('dash_component', 'list'))
}

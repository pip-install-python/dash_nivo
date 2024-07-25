# AUTO GENERATED FILE - DO NOT EDIT

#' @export
areaBump <- function(id=NULL, axisBottom=NULL, axisTop=NULL, blendMode=NULL, clickedPoint=NULL, colors=NULL, data=NULL, defs=NULL, endLabel=NULL, fill=NULL, margin=NULL, spacing=NULL, startLabel=NULL) {
    
    props <- list(id=id, axisBottom=axisBottom, axisTop=axisTop, blendMode=blendMode, clickedPoint=clickedPoint, colors=colors, data=data, defs=defs, endLabel=endLabel, fill=fill, margin=margin, spacing=spacing, startLabel=startLabel)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'AreaBump',
        namespace = 'dash_nivo',
        propNames = c('id', 'axisBottom', 'axisTop', 'blendMode', 'clickedPoint', 'colors', 'data', 'defs', 'endLabel', 'fill', 'margin', 'spacing', 'startLabel'),
        package = 'dashNivo'
        )

    structure(component, class = c('dash_component', 'list'))
}

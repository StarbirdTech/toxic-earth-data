let data = []
let yearStart = 2012
let yearEnd = 2021
let yearCount

function preload() {
    yearCount = yearEnd - yearStart
    for (let i = 0; i < yearCount; i++) {
        data.push(loadTable("data/data_" + (yearStart + i) + ".csv", "csv", "header"));
    }
}

function setup() {
    createCanvas(800, 400);
    background(0);
    fill(125);

    data.forEach((yearData, dataIndex) => {
        yearData.getRows().forEach((element) => {
            circle(map(element.getNum(1), -180, 180, 0, 800), map(element.getNum(0), 90, -90, 0, 400), 0.1);
        });
        save('fire-' + (yearStart + dataIndex) + '.jpg')
    })
}

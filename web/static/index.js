var listAPI = '/list.json'
var imgAPI = './api/modal.json'

var app = new Vue({
    el: '#app',
    data: {
        lists: [],
        dataset: {
            title: 'NASAMIA',
            info: 'An open source project aims to show the world the data.'
        }
    }
})

function xhrGet(path, callback) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200)
            callback(this.responseText);
    }
    xhttp.open("GET", path, true);
    xhttp.send();
}

xhrGet(listAPI, (response) => {
    list = JSON.parse(response);
    for (i = 0; i < list.length; i++)
        app.lists.push({
            title: list[i].title,
            src: '?dataset=' + list[i].src
        })
});

var dropdown = document.querySelector('.dropdown');

dropdown.addEventListener('click', function (event) {
    event.stopPropagation();
    dropdown.classList.toggle('is-active');
});

var url = new URL(window.location.href);
var dataset = url.searchParams.get("dataset");
var fill = {},
    data = {},
    bubble = [],
    map, modal_info = {};

if (dataset)
    xhrGet(dataset, (response) => {
        console.log(response);
        j = JSON.parse(response);
        document.title = j.title;

        app.dataset = j;

        fill = {
            defaultFill: '#DDDDDD'
        };
        for (i = 0; i < j.geography.length; i++) {
            fill[j.geography[i].color] = j.geography[i].color
            data[j.geography[i].country] = {
                fillKey: j.geography[i].color,
                info: j.geography[i].info,
                modal_info: j.geography[i].modal_info
            };
        }

        for (i = 0; i < j.bubbles.length; i++) {
            fill[j.bubbles[i].color] = j.bubbles[i].color;
            bubble.push({
                name: j.bubbles[i].name,
                latitude: j.bubbles[i].latitude,
                longitude: j.bubbles[i].longitude,
                radius: j.bubbles[i].radius,
                fillKey: j.bubbles[i].color,
                info: j.bubbles[i].info
            })
        }

        map = new Datamap({
            element: document.getElementById('container'),
            fills: fill,
            geographyConfig: {
                highlightFillColor: 'rgba(50, 50, 50, 0.8)',
                highlightBorderColor: 'rgba(0, 0, 0, 0)',
                popupTemplate: function (geography, data) {
                    if (data)
                        return '<div class="hoverinfo"><strong>' + geography.properties.name +
                            '</strong><br>' + data.info;
                    return '<div class="hoverinfo"><strong>' + geography.properties.name +
                        '</strong><br>';
                }
            },
            data: data,
            bubblesConfig: {
                highlightFillColor: '#000000',
                highlightBorderColor: '#000000'
            },
            done: function (datamap) {
                datamap.svg.selectAll('.datamaps-subunit').on('click', function (geography) {
                    modal(geography.properties.country, data[geography.id].modal_info);
                });
            }
        });

        map.bubbles(bubble, {
            popupTemplate: function (geo, data) {
                return "<div class='hoverinfo'><strong>" + data.name + "</strong><br>" + data.info;
            }
        });
    })
else
    map = new Datamap({
        element: document.getElementById('container'),
        fills: {
            defaultFill: '#DDDDDD'
        },
        geographyConfig: {
            highlightFillColor: 'rgba(50, 50, 50, 0.8)',
            highlightBorderColor: 'rgba(0, 0, 0, 0)',
            popupTemplate: function (geography, data) {
                if (data)
                    return '<div class="hoverinfo"><strong>' + geography.properties.name +
                        '</strong><br>' + data.info;
                return '<div class="hoverinfo"><strong>' + geography.properties.name +
                    '</strong><br>';
            }
        },
        data: data,
        bubblesConfig: {
            highlightFillColor: '#000000',
            highlightBorderColor: '#000000'
        }
    });

function redirect() {
    console.log('https://www.csie.ntu.edu.tw/~b08902143/nasamia/?dataset=' + document.getElementById('url').value);
    window.location.href = 'https://www.csie.ntu.edu.tw/~b08902143/nasamia/?dataset=' + document.getElementById('url').value;
}

function modal(title, content) {
    if (content != undefined) {
        document.getElementById('modal-title').innerHTML = title;
        document.getElementById('modal-content').innerHTML = content;
        document.getElementById('modal').classList.toggle('is-active')
    }
}

function xhrModal(path){
    console.log(path);
    xhrGet(path, (res)=>{
        json = JSON.parse(res);
        modal(json.title, json.modal_content);
    })
}
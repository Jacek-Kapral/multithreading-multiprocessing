poczatekraportu = """<html>
    <head>
    <title>Jacek Cierkosz - Multithreading/Multiprocessing
    benchmark results</title>
    <style>
    
    #snow {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    pointer-events: none;
    z-index: 1000;
    }
    
    body {
      font-size: 10pt;
    }

    h2 {
      padding-top: 10pt;
    }

    table {
      font-family: arial, sans-serif;
      border-collapse: collapse;
      width: 100%;
      table-layout: fixed ;
    }

    td, th {
      border: 2px solid #b9b9b9;
      padding: 10px;
      text-align: center;
      width: 25% ;
    }

    th {
      background-color: #d5d5d5;
    }

    td {
    }

    tr:nth-child(odd) {
      background-color: #e5e5e5;
    }
    tr:nth-child(even) {
      background-color: #b0b0b0;
    }

    </style>
    <div id="snowflakeContainer">
        <span class="snowflake"></span>
    </div>
    <script>
    document.addEventListener('DOMContentLoaded', function(){
        var script = document.createElement('script');
        script.src = 'https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js';
        script.onload = function(){
            particlesJS("snow", {
                "particles": {
                    "number": {
                        "value": 200,
                        "density": {
                            "enable": true,
                            "value_area": 800
                        }
                    },
                    "color": {
                        "value": "#ffffff"
                    },
                    "opacity": {
                        "value": 0.7,
                        "random": false,
                        "anim": {
                            "enable": false
                        }
                    },
                    "size": {
                        "value": 5,
                        "random": true,
                        "anim": {
                            "enable": false
                        }
                    },
                    "line_linked": {
                        "enable": false
                    },
                    "move": {
                        "enable": true,
                        "speed": 5,
                        "direction": "bottom",
                        "random": true,
                        "straight": false,
                        "out_mode": "out",
                        "bounce": false,
                        "attract": {
                            "enable": true,
                            "rotateX": 300,
                            "rotateY": 1200
                        }
                    }
                },
                "interactivity": {
                    "events": {
                        "onhover": {
                            "enable": false
                        },
                        "onclick": {
                            "enable": false
                        },
                        "resize": false
                    }
                },
                "retina_detect": true
            });
        }
        document.head.append(script);
    });
    </script>
    </head>
    <body bgcolor=black>
    <div id="snow"></div>
    <font color = silver>

    <h1><marquee>Multithreading/Multiprocessing
     benchmark results</marquee></h1>
    <p>
    </p>

    <h2>Środowisko testowe:</h2>
    <p>
"""

naglowektabeli = """
<h2>Wyniki testu:</h2>
<img src = "hams.gif" width="216" height="72" />
<p>Poniższa tabela zawiera wyniki testu:</p>
<table>
  <tr>
    <th>Które wykonanie:</th>
    <th>1&nbsp;wątek</th>
    <th>4&nbsp;wątki</th>
    <th>4&nbsp;procesy</th>
    <th>Wszystkie dostępne procesy:</th>
  </tr>
"""

td = """<td>"""
ntd = """</td>"""
tr = """<tr>"""
ntr = """</tr>"""
ntb = """</table>"""

hams = """<img src = "hams.gif" width="216" height="72" />"""

medianka = """<h2>Podsumowanie:</h2>
<p>Poniższa tabela zawiera zestawienie median z rezultatów badania:</p>
<table>
    <tr>
        <th>Wykonanie:</th>
        <th>1&nbsp;wątek</th>
        <th>4&nbsp;wątki</th>
        <th>4&nbsp;procesy</th>
        <th>Wszystkie dostępne procesy:</th>
    </tr>
"""

stopka = """
<p>Autor aplikacji: Jacek Cierkosz</p>
</body></html>
"""
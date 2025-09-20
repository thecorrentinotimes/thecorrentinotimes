import feedparser
from datetime import datetime

# Lista de feeds RSS (cambialos por los tuyos)
RSS_FEEDS = [
    'https://www.corrienteshoy.com/feed/',
    'https://www.radiodos.com.ar/feed/'
    # Agregá tus feeds aquí, ej.: 'https://www.ellitoral.com.ar/rss/'
]

def generar_noticias_html():
    all_items = []
    for feed_url in RSS_FEEDS:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries[:5]:  # Máximo 5 por feed
            all_items.append({
                'title': entry.get('title', 'Sin título'),
                'link': entry.get('link', '#'),
                'description': entry.get('summary', entry.get('description', 'Sin descripción'))[:150] + '...',
                'pubDate': entry.get('published', 'Desconocida'),
                'source': feed.feed.get('title', 'Desconocida')
            })

    # Ordena por fecha (maneja fechas faltantes)
    all_items.sort(key=lambda x: x.get('pubDate', ''), reverse=True)

    # Generar HTML con la misma estructura de index.html
    html = '''
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>Noticias - The Correntino Times</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <link rel="stylesheet" type="text/css" href="assets/font/font-awesome.min.css" />
        <link rel="stylesheet" type="text/css" href="assets/font/font.css" />
        <link rel="stylesheet" type="text/css" href="assets/css/bootstrap.min.css" media="screen" />
        <link rel="stylesheet" type="text/css" href="assets/css/style.css" media="screen" />
        <link rel="stylesheet" type="text/css" href="assets/css/responsive.css" media="screen" />
        <link rel="stylesheet" type="text/css" href="assets/css/jquery.bxslider.css" media="screen" />
    </head>
    <body>
    <div class="body_wrapper">
        <div class="center">
            <div class="header_area">
                <div class="logo floatleft"><a href="index.html"><img src="images/logo.png" alt="" /></a></div>
                <div class="top_menu floatleft">
                    <ul>
                        <li><a href="index.html">Home</a></li>
                        <li><a href="#">About</a></li>
                        <li><a href="#">Contact us</a></li>
                        <li><a href="#">Subscribe</a></li>
                        <li><a href="#">Login</a></li>
                    </ul>
                </div>
                <div class="social_plus_search floatright">
                    <div class="social">
                        <ul>
                            <li><a href="#" class="twitter"></a></li>
                            <li><a href="#" class="facebook"></a></li>
                            <li><a href="#" class="feed"></a></li>
                        </ul>
                    </div>
                    <div class="search">
                        <form action="#" method="post" id="search_form">
                            <input type="text" value="Search news" id="s" />
                            <input type="submit" id="searchform" value="search" />
                            <input type="hidden" value="post" name="post_type" />
                        </form>
                    </div>
                </div>
            </div>
            <div class="main_menu_area">
                <ul id="nav">
                    <li><a href="#">world news</a></li>
                    <li><a href="#">sports</a></li>
                    <li><a href="#">tech</a></li>
                    <li><a href="#">business</a></li>
                    <li><a href="#">Movies</a></li>
                    <li><a href="#">entertainment</a></li>
                    <li><a href="#">culture</a></li>
                    <li><a href="#">Books</a></li>
                    <li><a href="#">classifieds</a></li>
                    <li><a href="#">blogs</a></li>
                    <li><a href="noticias.html">noticias</a></li>
                </ul>
            </div>
            <div class="content_area">
                <div class="main_content floatleft">
                    <div class="single_left_coloum_wrapper">
                        <h2 class="title">Últimas Noticias</h2>
                        <a class="more" href="#">more</a>
    '''
    for item in all_items[:10]:
        html += f'''
                        <div class="single_left_coloum floatleft">
                            <h3>{item['title']}</h3>
                            <p>{item['description']}</p>
                            <p><small>{item['pubDate']} - Fuente: {item['source']}</small></p>
                            <a class="readmore" href="{item['link']}" target="_blank">read more</a>
                        </div>
        '''
    html += '''
                    </div>
                </div>
                <div class="sidebar floatright">
                    <div class="single_sidebar">
                        <div class="news-letter">
                            <h2>Sign Up for Newsletter</h2>
                            <p>Sign up to receive our free newsletters!</p>
                            <form action="#" method="post">
                                <input type="text" value="Name" id="name" />
                                <input type="text" value="Email Address" id="email" />
                                <input type="submit" value="SUBMIT" id="form-submit" />
                            </form>
                            <p class="news-letter-privacy">We do not spam. We value your privacy!</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="footer_bottom_area">
                <div class="copyright_text">
                    <p>Copyright &copy; 2025 The Correntino Times Inc. All rights reserved</p>
                </div>
            </div>
        </div>
    </div>
    <script type="text/javascript" src="assets/js/jquery-min.js"></script>
    <script type="text/javascript" src="assets/js/bootstrap.min.js"></script>
    <script type="text/javascript" src="assets/js/jquery.bxslider.js"></script>
    <script type="text/javascript" src="assets/js/selectnav.min.js"></script>
    <script type="text/javascript">
    selectnav('nav', {
        label: '-Navigation-',
        nested: true,
        indent: '-'
    });
    $('.bxslider').bxSlider({
        mode: 'fade',
        captions: true
    });
    </script>
    </body>
    </html>
    '''
    with open('noticias.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    generar_noticias_html()
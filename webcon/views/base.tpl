<html>
  <head>
    <meta charset="utf-8">
    <title>{{title or 'webcon'}}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" href="/static/css/skeleton/normalize.css">
    <link rel="stylesheet" type="text/css" href="/static/css/skeleton/skeleton.css">
    <link rel="stylesheet" type="text/css" href="/static/css/style.css">
    <script>
    const post = (url) => {
      document.getElementById('output').textContent = '=== SENDING ==='
      fetch(url, {method: 'post'})
        .then((r) => r.text())
        .then((t) => document.getElementById('output').textContent = t)
    }
    </script>
  </head>
  <body>
    <div class="container">
      {{!base}}
    </div>
  </body>
</html>

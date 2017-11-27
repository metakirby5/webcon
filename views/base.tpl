<html>
  <head>
    <title>{{title or 'webcon'}}</title>
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
  <body>{{!base}}</body>
</html>

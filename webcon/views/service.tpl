% rebase('base.tpl', title=title)
<h1>{{title}}</h1>
<div class="button-stack">
  % for action, path in actions:
  <button onclick="post('{{path}}')">{{action}}</button>
  % end
  <a class="button button-primary" href="/">Index</a>
</div>

<pre><code id="output">Command output will display here.</code></pre>

<script>
const post = async (url) => {
  const $output = document.getElementById('output')
  $output.className = ''
  $output.textContent = 'Dispatching command...'

  const response = await fetch(url, {
    method: 'post',
    credentials: 'same-origin'
  })

  $output.textContent = await response.text() || 'No output.'
  $output.classList.add(response.ok ? 'success' : 'error')
}
</script>

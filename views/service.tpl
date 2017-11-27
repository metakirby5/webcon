% rebase('base.tpl', title=title)
<h1>{{title}}</h1>
<div class="button-stack">
% for action, path in actions:
<button onclick="post('{{path}}')">{{action}}</button>
% end
<a class="button button-primary" href="/">Index</a>
</div>
<h2>Command output</h2>
<pre><code id="output"></code></pre>

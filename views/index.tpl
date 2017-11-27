% rebase('base.tpl', title='webcon')
<h1>Services</h1>
<div class="button-stack">
% for service, path in services:
<a class="button" href="{{path}}">{{service}}</a>
% end
</div>

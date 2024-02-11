---
title: "News"
layout: textlay
excerpt: "BIOMAC - News"
sitemap: false
permalink: allnews/
lang: en
---

# News

{% for article in site.data.news %}
<p>
<strong>
{{ article.date }}</strong>  --- {{ article.headline }} <br>
<em>{% if article.fullnews %}{{ article.fullnews }}<br>{% endif %}</em>
{% if article.image %}
<img src="{{ site.url }}{{ site.basurl }}/images/newspic/{{ article.image }}" class="img" height = "250px" width="auto"  style="float: left" alt = "sometext" />
<br><br><br><br><br><br><br><br><br><br><br><br><br>
{% endif %}
</p>
{% endfor %}


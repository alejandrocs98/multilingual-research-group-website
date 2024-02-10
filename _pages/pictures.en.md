---
title: "(Pics)"
layout: piclay
excerpt: "BCEM - Pics"
sitemap: false
permalink: pictures/
lang: en
inheader_order: 5
---

# Pictures
---

## Gallery

{% assign number_printed = 0 %}
{% for pic in site.data.pictures_gal %}

{% assign mod = number_printed | modulo: 3 %}

{% if mod == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-4 clearfix">
<img src="{{ site.url }}{{ site.baseurl }}/images/picpic/gallery/{{ pic.image }}" class="img-responsive" width="100%" style="float: left" />
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if mod == 2 %}
</div>
{% endif %}

{% endfor %}


{% if mod != 2 %}
</div>
{% endif %}

<p> &nbsp; </p>
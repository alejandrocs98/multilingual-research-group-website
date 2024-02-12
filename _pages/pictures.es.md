---
title: "(Pics)"
layout: piclay
excerpt: "BCEM - Pics"
sitemap: false
permalink: pictures/
lang: es
inheader_order: 5
---

# Fotos
---

## Galería

{% assign number_printed = 0 %}
{% for pic in site.data.pictures_gal %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
<img src="{{ site.url }}{{ site.baseurl }}/images/picpic/gallery/{{ pic.image }}" class="img-responsive" width="100%" style="float: left" />
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

---

## BCEM a lo largo de los años

{% for pic in site.data.pictures_gens %}

<div class="row">

<h3>{{pic.year}}</h3>

<div class="col-sm-12 clearfix">
<img src="{{ site.url }}{{ site.baseurl }}/images/picpic/gens/{{ pic.image }}" class="img-responsive" width="100%" style="float: left" />
</div>

</div>

{% endfor %}

<p> &nbsp; </p>
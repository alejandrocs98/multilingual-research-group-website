---
title: "Equipo"
layout: gridlay
excerpt: "BCEM - Equipo"
sitemap: false
permalink: team/
lang: es
inheader_order: 1
---

# Miembros del grupo

{% assign sorted_team = site.team | sort: "started" %}
{% assign number_printed = 0 %}
{% for member in sorted_team %}

{% if member.started and member.ended == nil %}

{% assign mod = number_printed | modulo: 3 %}

{% if mod == 0 %}
<div class="row">
{% endif %}

{% include team_member.html member=member %}

{% assign number_printed = number_printed | plus: 1 %}

{% if mod == 2 %}
</div>
{% endif %}

{% endif %}

{% endfor %}


{% if mod != 2 %}
</div>
{% endif %}

--- 
# Miembros anteriores

{% assign sorted_team = site.team | sort: "ended" | reverse %}
{% for member in sorted_team %}

{% if member.started and member.ended %}

{% include former_team_member.html member=member %}

{% endif %}

{% endfor %}

<br>
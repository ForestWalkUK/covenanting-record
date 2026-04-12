---
layout: default
title: "Documents"
---

<article>
    <h1>Documents</h1>
    <p class="subtitle">Longer works, papers, and transcriptions</p>

    <section>
        <p>
            These documents are longer or more formal works &mdash; transcriptions of
            historical Covenanting texts, essays, and structured papers &mdash; presented
            with sidebar navigation for ease of reading.
        </p>

        <ul class="post-list">
            {% assign docs = site.documents | sort: 'order' %}
            {% for doc in docs %}
            <li>
                <h3 class="post-title">
                    <a href="{{ doc.url | relative_url }}">{{ doc.title }}</a>
                </h3>
                {% if doc.subtitle %}
                <p class="post-meta"><em>{{ doc.subtitle }}</em></p>
                {% endif %}
                {% if doc.description %}
                <p class="post-excerpt">{{ doc.description }}</p>
                {% endif %}
            </li>
            {% endfor %}
        </ul>
    </section>
</article>

---
layout: default
title: "The Covenanting Record"
---

<article>
    <h1>The Covenanting Record</h1>
    <p class="subtitle">A journal of Reformed and Covenanting reflection</p>

    <section>
        <p>
            These are the written reflections of a soul of the remnant &mdash; one who holds
            to the Solemn League and Covenant, the Westminster Standards, and the Covenanting
            testimony of the Church of Scotland. They are offered in the spirit of those who
            have gone before, whose blood was the seed of the Kirk, and whose writings yet
            speak though they are gone.
        </p>
        <p>
            <em>&#8220;Remember them which have the rule over you, who have spoken unto you
            the word of God: whose faith follow, considering the end of their conversation.&#8221;</em>
            <br><small style="color:#888;">Hebrews 13:7</small>
        </p>
    </section>

    <hr>

    <h2>Journal Entries</h2>

    <ul class="post-list">
        {% for post in site.posts %}
        <li>
            <h3 class="post-title">
                <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
            </h3>
            <p class="post-meta">{{ post.date | date: "%-d %B %Y" }}</p>
            {% if post.excerpt %}
            <p class="post-excerpt">{{ post.excerpt | strip_html | truncatewords: 50 }}</p>
            {% endif %}
        </li>
        {% endfor %}
    </ul>

</article>

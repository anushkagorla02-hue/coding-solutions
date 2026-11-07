# DPLEARN54 - Rating 1150

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Hamburger Menu Challenge

Welcome to the  **Sleek Hamburger Menu**  Challenge!

Chef has just begun his journey into the  **Spider-Verse Developer**  Missions. 🍝🕷️
To organize his growing collection of web pages, he’s designed a sleek navigation sidebar — a modern  **hamburger menu**  that appears beautifully on all screens, from mobiles to desktops.

But there’s one catch — the menu isn’t functional yet!
Clicking the hamburger icon doesn’t open the sidebar. Chef needs your help to bring this interactive feature to life.

Your mission is to make the  **hamburger menu functional**, enabling it to toggle smoothly between open and closed states.

 **Project Overview:** 
Your project folder includes:

- index.html - The webpage structure, containing all major sections (Hero, About, Tracks, Schedule, Leaderboard, and Footer).
- style.css - The complete styling of the page, with transitions and responsive layouts already set up.
- script.js - A partially written file where your logic will go.

Here’s what’s already working:

- The hero section, images, and animations are fully styled.
- The hamburger icon (.hamburger) and the sidebar menu (.menu) are present in the HTML.
- Smooth animations and layout transitions are predefined in CSS.

However, the menu functionality is missing — it doesn’t open or close when clicked. That’s where you come in.

 **Your Tasks:** 

- Complete the Sidebar Menu in HTML
- Inside the <div class="menu" id="menu">, you’ll find an empty list (<ul>).
- Add menu items for the key sections: Home, Missions, Spider-Verse Hub, Progress, Resources, and Contact.
- Each item should link to its respective section (for now, simple # links are fine). Docs: MDN - HTML
- Implement the Toggle Logic in JavaScript
- In the script.js file, select both the hamburger and menu elements.
- Add a click event listener to the hamburger icon.
- When clicked, toggle an active class on both the hamburger and the menu.
- This will allow the menu to slide in and out based on user interaction. Docs: MDN – Event Listener, MDN – DOM Selection, MDN – ClassList Property
- Add the Missing CSS Animations
- In the style.css file, locate the styles for.hamburger and.menu.
- Add animation rules so that: The hamburger icon smoothly transforms into an “X” when the menu is active. The middle bar of the hamburger disappears during this transition. The sidebar menu slides into view when active and hides when inactive.
- Use the.active class to trigger these transitions. Docs: MDN – CSS Transform, MDN – nth-child Selector, MDN – Opacity Property

 **Expected Behaviour:**

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-07T14:58:09.375Z  

```cpp
    </p>
    <p>
      Step forward, Developer. The <b>Spider-Verse</b> has opened its gates — and this is where your mission begins.
    <p>
      The web is your canvas — each tag, each style, and each interaction forms a part of your story.  
      Just as Spider-Man connects worlds with his web, developers connect users through their creations.
  <section class="content leaderboard">
    <h2>Begin Your Journey</h2>
  </section>

  <!-- Closing Note -->
      <p>🕸️ Learn how visual hierarchy and motion guide user interaction.</p>
      <p>🕷️ Prepare for advanced Spider-Verse challenges involving interactivity and animation.</p>
    </div>
      <p>🕸️ Understand and implement structured layouts that adapt across devices.</p>
      <p>🕷️ Strengthen knowledge of responsive design and interface fundamentals.</p>
  <section class="content schedule">
    <h2>Developer Objectives</h2>
    <div class="objectives-list">

  <!-- Mission Objectives -->
      Guided by the mysterious “Web-Slinger 42,” his training begins here.
    </p>
  </section>
    <p>
      The message was clear: *“Every web has a pattern. Every developer has a mission.”*  
      With that, Chef accepted the call — stepping into a multidimensional world of design, logic, and creativity.  
```

---

[View on CodeChef](https://www.codechef.com/problems/DPLEARN54)
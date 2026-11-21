---
name: ig-caption
description: >-
  Write the Instagram caption - the line that survives the "... more" cut, the
  body, the single ask and the search terms (no hashtags, GRØNN rule) - and lint it
  before it goes out. Use when the user says "write the caption", "caption this",
  "what do I put in the description", has a reel or a carousel ready and needs
  the text, or asks about hashtags.
---

# ig-caption

> **GRØNN:** lees eerst `templates/voice.md` in deze plugin (twee mappen boven
> deze skill), of `~/.claude/instagram/voice.md` als die bestaat. Die huisregels
> gaan voor alles hieronder: Nederlands, geen hashtags, nooit twee keer dezelfde
> emoji, dienst + plaats in de tekst, niets hergebruiken, nooit publiceren.

One tool lives in this folder and it runs:

```bash
python3 caption.py caption.txt
python3 caption.py caption.txt --keywords "vijver,Stein"
```

It prints the caption the way the feed prints it: the first 125 characters in a
box, everything else behind the tap. Read that box before you read anything
else you wrote.

## First, decide which job this caption has

This is the decision that ruins captions when it is skipped.

**Job A: the video already hooked them.** A Reel carries its own hook in the
first two seconds, spoken and on screen. The caption is not a second hook and
competing with the video is how you lose both. Its job is the ask, the context
that makes the ask make sense, and the words people search.

**Job B: the caption is the content.** A photo, a single image, a carousel
cover that opens a loop. Here line one is the hook and it works exactly like a
Reel hook: concrete, short, and cut off at a cliff rather than mid-clause.

Ask which one you are writing. If the user has a Reel with a strong hook,
write A and say why.

## The shape

```
Line 1      125 characters of visible space. Job A: the ask, plainly.
            Job B: the hook.
            Never a greeting, never a hashtag, never an emoji as the first
            character.
Body        short paragraphs, one line of white space between each. Two to six
            of them. This is where the search terms live.
The ask     one. For GRØNN almost always: stuur een foto (WhatsApp). One.
Hashtags    none. GRØNN uses no hashtags.
```

Limit is 2,200 characters and almost nothing needs 2,200. A caption that earns
the tap and then delivers 600 characters beats one that delivers 1,800.

## Hashtags: none

GRØNN uses no hashtags (Nick, 9 November 2026). Instagram itself says they are
a label, not a reach lever, and capped them at five per post on 18 December
2025. `caption.py` fails any caption with a hashtag in it.

## Search terms do the work instead

Instagram search reads the caption text. So what Nick does and where goes in
the caption as a phrase a human would type, in a sentence that reads normally:
"vijver in Stein", "natuurlijke tuin in Elsloo". Always one service and one
place in "Stein en omgeving". `caption.py` checks that on its own
(DIENST + PLAATS); pass the exact terms when you want them checked too:

```bash
python3 caption.py draft.txt --keywords "vijverrenovatie,Stein"
```

## Rules

- **No link in the caption.** Captions are not clickable. A URL in the body is
  dead text that says "I do not use this platform". Bio or DM.
- **One ask.** Two asks is the same as none. `caption.py` counts them.
- **The keyword ask needs a keyword people can type.** One word, no spaces, no
  emoji, and say it out loud in the video too. `Comment CONTRACT` works.
  `Comment "the contract guide"` does not.
- **Write the first comment separately** if there is a link. Say so in the
  receipt.
- **Emoji yes, but never the same one twice.** Not in one caption, and not in
  this week's other captions (check `~/.claude/instagram/log.md`). The linter
  fails a repeated emoji and flags anything over 4 per 100 characters.
- **Dutch by default.** Quote posts carry English on the image; the caption
  under them may stay Dutch.
- **Never reuse text.** No hook or sentence that was already posted.
- **Alt text is worth 20 seconds.** For carousels and photos, write it. It is
  read by screen readers and by Instagram.

## The loop

1. Decide Job A or Job B and say which.
2. Draft it.
3. Run `/ig-human` on it. Captions are short, so slop is louder here than
   anywhere else in the pack.
4. Run `caption.py` with the user's search terms. Fix every FAIL. Decide on
   every WARN out loud rather than silently.
5. Print the copy-ready block, then the receipt:

```
CAPTION READY
job:        A - the reel carries the hook
visible:    118 of 125 characters used before the cut
ask:        one, stuur een foto
hashtags:   0
emoji:      2, all different
search:     "vijver" and "Stein" in line 1
linter:     READY
```

Nothing is posted. Deliver the caption as text (and images as loose files);
Nick uploads it himself. Add the hook and the photos used to
`~/.claude/instagram/log.md` so they are never used again.

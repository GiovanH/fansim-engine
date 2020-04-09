## Text retcon

```
    gam neutral1 "XXXXXXXXXXXXXXXXXXXXXXX AAAAAAAAAAAAAAAAA{nw}"
    $ _history_list.pop()
    gam neutral1 "XXXXXXXXXXXXXXXXXXXXXXX{fast} BBBBBBBBBBBBBBB"
```

On line 1, text proceeds as normal until it hits the `{nw}` mark, where it instantly skips to the next line, not waiting for the user.
The second line pops that line from the history scrollbac, so the user doesn't see it in the chat logs.
On the third line, all the text up through the `{fast}` mark is displayed instantly.

This has the effect of erasing the AAAAAAAAAAAAAAAAA mark and replacing it with BBBBBBBBBBBBBBB in real time.


# -*- coding: utf-8 -*-
from pathlib import Path


def find_detail_end(text: str, start: int) -> int:
    depth = 0
    i = start
    n = len(text)
    while i < n:
        if text.startswith("<details", i):
            depth += 1
            i += 8
            continue
        if text.startswith("</details>", i):
            depth -= 1
            i += 10
            if depth == 0:
                return i
            continue
        i += 1
    raise RuntimeError("unbalanced details")


def replace_detail_by_id(text: str, fragment: str) -> str:
    needle = 'id="'
    q = fragment.index(needle) + len(needle)
    end_id = fragment.index('"', q)
    pid = fragment[q:end_id]
    marker = f'id="{pid}"'
    s = text.find(marker)
    if s < 0:
        raise SystemExit(f"missing {pid}")
    s = text.rfind("<details", 0, s)
    e = find_detail_end(text, s)
    return text[:s] + fragment.strip() + "\n\n" + text[e:]


def main():
    root = Path(__file__).resolve().parent.parent
    wiki = root / "wiki.html"
    text = wiki.read_text(encoding="utf-8")
    cu = (root / "tools" / "wiki_options_fragment.html").read_text(encoding="utf-8")
    dm = (root / "tools" / "wiki_dust765_fragment.html").read_text(encoding="utf-8")
    aux = (root / "tools" / "wiki_aux_fragment.html").read_text(encoding="utf-8")

    cu_block = cu.strip() + "\n\n"
    start_general = '      <details class="wiki-article" id="wiki-opt-general">'
    dust_open = '      <details class="wiki-article" id="wiki-opt-dust">'
    if start_general in text:
        s = text.find(start_general)
        e = text.find(dust_open)
        if e < 0:
            raise SystemExit("wiki-opt-dust marker missing")
        text = text[:s] + cu_block + text[e:]
    else:
        needle = "\n\n" + dust_open
        if needle not in text:
            raise SystemExit("insert marker missing")
        text = text.replace(needle, "\n\n" + cu + dust_open, 1)

    s = text.find('id="wiki-opt-dust"')
    s = text.rfind("<details", 0, s)
    e = text.find('id="wiki-opt-mods"')
    e = text.rfind("<details", 0, e)
    e = find_detail_end(text, e)
    text = text[:s] + dm.strip() + "\n\n" + text[e:]

    for part in aux.split("      <details "):
        if not part.strip():
            continue
        frag = "      <details " + part
        frag = frag.rstrip()
        if not frag.endswith("</details>"):
            frag = frag[: frag.rindex("</details>") + len("</details>")]
        text = replace_detail_by_id(text, frag)

    wiki.write_text(text, encoding="utf-8")
    print("updated", wiki)


if __name__ == "__main__":
    main()

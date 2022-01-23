# This is a sample Python script.
import os

import click
import dateutil.parser
import markdownify
import xmltodict


def eject_hugo(entry, hugo_dir):
    title = entry['title']
    link = entry['link']
    link_parts = link.split('/')
    filename = f'{hugo_dir}/{link_parts[3]}-{link_parts[4]}-{link_parts[5]}-{link_parts[-1]}.md'
    tags = entry['category']
    content = entry['content:encoded']
    content_md = markdownify.markdownify(content, heading_style='ATX')
    timestamp = dateutil.parser.parse(entry['pubDate']).strftime('%FT%T%z')
    with open(filename, 'wt') as hugo:
        print('---', file=hugo)
        print(f'title: "{title}"', file=hugo)
        print(f'date: {timestamp}', file=hugo)
        if tags:
            print('tags:', file=hugo)
            for t in tags:
                print(f'  - {t}', file=hugo)
        print('---\n', file=hugo)
        print(content_md, file=hugo)


@click.command()
@click.argument('rss_feed', type=click.Path(exists=True, dir_okay=False, readable=True, resolve_path=True))
@click.argument('hugo_dir', type=click.Path(file_okay=False, resolve_path=True))
def cli(rss_feed, hugo_dir):
    rss = None
    if not os.path.exists(hugo_dir):
        os.makedirs(hugo_dir)
    with open(rss_feed, 'rb') as r:
        rss = xmltodict.parse(r)
    for entry in rss['rss']['channel']['item']:
        print(f'- converting {entry["title"]}')
        eject_hugo(entry=entry, hugo_dir=hugo_dir)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cli()

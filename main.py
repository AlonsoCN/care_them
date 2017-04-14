import click

@click.group()
def start_application():
    """ CARE APP: Application to detect twits with emotional problems"""
    pass

@click.command()
@click.option('--path', default=None, help="YAML Configuration path file.")
def load_configuration(path):
    if path is None:
        click.echo('You must to define a correct path file. (i.e. --path)')
    else:
        click.echo('loading :)')

start_application.add_command(load_configuration)

if __name__ == '__main__':
    start_application()

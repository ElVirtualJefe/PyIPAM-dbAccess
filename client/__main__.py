import click
import cli
from text_client import TextClient

_client = TextClient()

@click.command()
@click.argument('id')
def _get_ip_address_by_id(id):
    click.echo(id)
    click.echo(_client.get_ip_address_by_id(id))

_cmds = {
    'get_ip_address_by_id': _get_ip_address_by_id
}

class _GrpcTextClientCli(click.MultiCommand):
    def list_commands(self, ctx):
        return sorted(list(_cmds.keys()))
    #
    def get_command(self, ctx, name):
        return _cmds[name]

cli = _GrpcTextClientCli(help='Text client commands')

cli()

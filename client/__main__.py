from email.policy import default
import string
import click
#import cli
from text_client import TextClient

_client = TextClient()

@click.group()
def write():
    pass

@write.group()
@click.argument('ip')
@click.argument('is_gateway', type=bool, default=False)
@click.argument('description', default='')
@click.argument('hostname', default='')
@click.argument('mac', default='')
@click.argument('owner', default='')
def _add_new_ip_address(ip,is_gateway,description,hostname,mac,owner):
    click.echo(_client.add_new_ip_address(ip,is_gateway,description,hostname,mac,owner))

@write.group()
@click.argument('tablename')
def _write_to_table(tablename):
    click.echo(_client.write_to_table(tableName=tablename))

@click.group()
def read():
    pass

@click.command()
@click.argument('id')
def _get_ip_address_by_id(id):
    click.echo("Searching for IP Address with ID: %s" % id)
    click.echo(_client.get_ip_address_by_id(id))

_cmds = {
    'get_ip_address_by_id': _get_ip_address_by_id,
    'add_new_ip_address': _add_new_ip_address,
    'write_to_table' : _write_to_table
}

class _GrpcTextClientCli(click.MultiCommand):
    def list_commands(self, ctx):
        return sorted(list(_cmds.keys()))
    #
    def get_command(self, ctx, name):
        return _cmds[name]

cli = _GrpcTextClientCli(help='Text client commands')

cli()

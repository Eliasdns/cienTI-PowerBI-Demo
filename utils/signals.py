from django.db.models.signals import post_save  # post_delete
from django.db import models
from utils.powerbi import push_stream_csv, push_stream_api


def apply_auto_push(model: type[models.Model]):
    post_save.connect(push_item_to_csv, sender=model)
    post_save.connect(push_aggregates_to_api, sender=model)
    # post_delete.connect(delete_item_from_csv, sender=model)


def push_item_to_csv(sender, instance, **kwargs):
    # TODO: Adicionar linha apenas caso create (o id não exista), Alterar caso contrário
    push_stream_csv(instance.obj_as_payload)


def push_aggregates_to_api(sender, instance, **kwargs):
    push_stream_api([type(instance).objects.aggs_as_payload()])

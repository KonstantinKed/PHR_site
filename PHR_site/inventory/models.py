# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Apartments(models.Model):
    apt_id = models.CharField(primary_key=True, max_length=2)
    apt_name = models.CharField(max_length=15)

    class Meta:
        managed = True
        db_table = 'apartments'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Condition(models.Model):
    cond_id = models.SmallAutoField(primary_key=True)
    cond_name = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'condition'


class Connection(models.Model):
    conn_id = models.IntegerField(primary_key=True)
    conn_name = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'connection'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class InventoryApartments(models.Model):
    id = models.BigAutoField(primary_key=True)
    apt_id = models.CharField(max_length=2)
    apt_name = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'inventory_apartments'


class InventoryCondition(models.Model):
    id = models.BigAutoField(primary_key=True)
    cond_id = models.IntegerField()
    cond_name = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'inventory_condition'


class Location(models.Model):
    loc_id = models.IntegerField(primary_key=True)
    loc_name_eng = models.CharField(max_length=25, blank=True, null=True)
    loc_name_ua = models.CharField(max_length=35, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location'


class Pics(models.Model):
    pics_id = models.SmallAutoField(primary_key=True)
    pics_link_1 = models.CharField(max_length=255, blank=True, null=True)
    pics_link_2 = models.CharField(max_length=255, blank=True, null=True)
    pics_link_3 = models.CharField(max_length=255, blank=True, null=True)
    pics_link_4 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pics'


class Type(models.Model):
    type_id = models.IntegerField(primary_key=True)
    type_name = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'type'
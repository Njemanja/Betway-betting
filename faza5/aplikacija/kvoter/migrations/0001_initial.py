# Generated by Django 4.0.4 on 2022-05-24 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Korisnik',
            fields=[
                ('idkor', models.IntegerField(db_column='IDKor', primary_key=True, serialize=False)),
                ('korisnickoime', models.CharField(blank=True, db_column='KorisnickoIme', max_length=20, null=True, unique=True)),
                ('ime', models.CharField(blank=True, db_column='Ime', max_length=20, null=True)),
                ('prezime', models.CharField(blank=True, db_column='Prezime', max_length=20, null=True)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=20, null=True)),
                ('lozinka', models.CharField(blank=True, db_column='Lozinka', max_length=2000, null=True)),
                ('jmbg', models.CharField(blank=True, db_column='JMBG', max_length=20, null=True, unique=True)),
                ('vip', models.IntegerField(blank=True, db_column='VIP', null=True)),
                ('kartica', models.CharField(blank=True, db_column='Kartica', max_length=20, null=True)),
                ('stanje', models.DecimalField(blank=True, db_column='Stanje', decimal_places=2, max_digits=15, null=True)),
            ],
            options={
                'db_table': 'korisnik',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Postavljenekvote',
            fields=[
                ('idkvo', models.CharField(db_column='IDKvo', max_length=18, primary_key=True, serialize=False)),
                ('kvota1', models.DecimalField(blank=True, db_column='Kvota1', decimal_places=2, max_digits=5, null=True)),
                ('kvotax', models.DecimalField(blank=True, db_column='KvotaX', decimal_places=2, max_digits=5, null=True)),
                ('kvota2', models.DecimalField(blank=True, db_column='Kvota2', decimal_places=2, max_digits=5, null=True)),
                ('kvota11', models.DecimalField(blank=True, db_column='Kvota11', decimal_places=2, max_digits=5, null=True)),
                ('kvota1x', models.DecimalField(blank=True, db_column='Kvota1X', decimal_places=2, max_digits=5, null=True)),
                ('kvota12', models.DecimalField(blank=True, db_column='Kvota12', decimal_places=2, max_digits=5, null=True)),
                ('kvotax1', models.DecimalField(blank=True, db_column='KvotaX1', decimal_places=2, max_digits=5, null=True)),
                ('kvotaxx', models.DecimalField(blank=True, db_column='KvotaXX', decimal_places=2, max_digits=5, null=True)),
                ('kvotax2', models.DecimalField(blank=True, db_column='KvotaX2', decimal_places=2, max_digits=5, null=True)),
                ('kvota21', models.DecimalField(blank=True, db_column='Kvota21', decimal_places=2, max_digits=5, null=True)),
                ('kvota2x', models.DecimalField(blank=True, db_column='Kvota2X', decimal_places=2, max_digits=5, null=True)),
                ('kvota22', models.DecimalField(blank=True, db_column='Kvota22', decimal_places=2, max_digits=5, null=True)),
                ('prvigol1', models.DecimalField(blank=True, db_column='PrviGol1', decimal_places=2, max_digits=5, null=True)),
                ('prvigol2', models.DecimalField(blank=True, db_column='PrviGol2', decimal_places=2, max_digits=5, null=True)),
                ('prvigol3', models.DecimalField(blank=True, db_column='PrviGol3', decimal_places=2, max_digits=5, null=True)),
            ],
            options={
                'db_table': 'postavljenekvote',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Statistika',
            fields=[
                ('idsta', models.IntegerField(db_column='IDSta', primary_key=True, serialize=False)),
                ('brojpogodjenih', models.IntegerField(db_column='BrojPogodjenih')),
                ('brojpromasenih', models.IntegerField(db_column='BrojPromasenih')),
                ('ukupnouplaceno', models.DecimalField(db_column='UkupnoUplaceno', decimal_places=2, max_digits=15)),
                ('ukupnodobijeno', models.DecimalField(db_column='UkupnoDobijeno', decimal_places=2, max_digits=15)),
                ('brojprimljenihpogodjenih', models.IntegerField(db_column='BrojPrimljenihPogodjenih')),
                ('brojprimljenihpromasenih', models.IntegerField(db_column='BrojPrimljenihPromasenih')),
            ],
            options={
                'db_table': 'statistika',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tiket',
            fields=[
                ('idtik', models.AutoField(db_column='IDTik', primary_key=True, serialize=False)),
                ('datumuplate', models.DateField(blank=True, db_column='DatumUplate', null=True)),
                ('iznosuplate', models.DecimalField(blank=True, db_column='IznosUplate', decimal_places=2, max_digits=10, null=True)),
                ('kvota', models.DecimalField(blank=True, db_column='Kvota', decimal_places=2, max_digits=15, null=True)),
                ('dobitak', models.DecimalField(blank=True, db_column='Dobitak', decimal_places=2, max_digits=15, null=True)),
            ],
            options={
                'db_table': 'tiket',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tiketdogadjaj',
            fields=[
                ('iddog', models.IntegerField(db_column='IDDog', primary_key=True, serialize=False)),
                ('odigrano', models.CharField(blank=True, db_column='Odigrano', max_length=20, null=True)),
                ('kvota', models.DecimalField(db_column='Kvota', decimal_places=2, max_digits=15)),
                ('ishod', models.IntegerField(blank=True, db_column='Ishod', null=True)),
            ],
            options={
                'db_table': 'tiketdogadjaj',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Utakmica',
            fields=[
                ('iduta', models.IntegerField(db_column='IDUta', primary_key=True, serialize=False)),
                ('datumpocetka', models.CharField(blank=True, db_column='DatumPocetka', max_length=30, null=True)),
                ('tim1', models.CharField(blank=True, db_column='Tim1', max_length=20, null=True)),
                ('tim2', models.CharField(blank=True, db_column='Tim2', max_length=20, null=True)),
            ],
            options={
                'db_table': 'utakmica',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Utakmica10',
            fields=[
                ('utakmica10', models.CharField(db_column='Utakmica10', max_length=100, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'utakmica10',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vipkvote',
            fields=[
                ('idkvo', models.AutoField(db_column='IDKvo', primary_key=True, serialize=False)),
                ('kvotaprolaz', models.DecimalField(blank=True, db_column='KvotaProlaz', decimal_places=2, max_digits=5, null=True)),
                ('kvotapad', models.DecimalField(blank=True, db_column='KvotaPad', decimal_places=2, max_digits=5, null=True)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('idkor', models.OneToOneField(db_column='IDKor', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='kvoter.korisnik')),
            ],
            options={
                'db_table': 'admin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Desetunizu',
            fields=[
                ('idkor', models.OneToOneField(db_column='IDKor', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='kvoter.korisnik')),
                ('brojpogodaka', models.IntegerField(blank=True, db_column='BrojPogodaka', null=True)),
                ('odigrano', models.CharField(blank=True, db_column='Odigrano', max_length=20, null=True)),
                ('validno', models.IntegerField(blank=True, db_column='Validno', null=True)),
            ],
            options={
                'db_table': 'desetunizu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Igrac',
            fields=[
                ('idkor', models.OneToOneField(db_column='IDKor', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='kvoter.korisnik')),
            ],
            options={
                'db_table': 'igrac',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Kvoter',
            fields=[
                ('idkor', models.OneToOneField(db_column='IDKor', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='kvoter.korisnik')),
            ],
            options={
                'db_table': 'kvoter',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Odigrano10Unizu',
            fields=[
                ('idkor', models.OneToOneField(db_column='IDKor', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='kvoter.korisnik')),
                ('ishod', models.IntegerField(db_column='Ishod')),
            ],
            options={
                'db_table': 'odigrano10unizu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Utakmiceunajavi',
            fields=[
                ('iduta', models.OneToOneField(db_column='IDUta', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='kvoter.utakmica')),
            ],
            options={
                'db_table': 'utakmiceunajavi',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Utakmiceutoku',
            fields=[
                ('iduta', models.OneToOneField(db_column='IDUta', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='kvoter.utakmica')),
            ],
            options={
                'db_table': 'utakmiceutoku',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Zavrseneutakmice',
            fields=[
                ('iduta', models.OneToOneField(db_column='IDUta', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='kvoter.utakmica')),
                ('ishod', models.IntegerField(db_column='Ishod')),
                ('poluvremekraj', models.CharField(db_column='PoluvremeKraj', max_length=3)),
                ('prvigol', models.CharField(db_column='PrviGol', max_length=1)),
            ],
            options={
                'db_table': 'zavrseneutakmice',
                'managed': False,
            },
        ),
    ]

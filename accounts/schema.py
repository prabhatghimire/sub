import graphene

from graphene_django.types import DjangoObjectType

from django.contrib.auth import get_user_model

from graphene import relay
from .models import User, Location
from django.db.models import Q
import datetime


class UserType(DjangoObjectType):
    class Meta:
        model = User
        exclude = ['is_staff', 'is_active', 'is_superuser', 'groups',
                   'user_permissions', 'last_login', 'password', 'donation_no','id', 'avatar']
        interfaces = (relay.Node, )

    """ @classmethod
    def get_queryset(cls, queryset, info):
        if info.context.user.is_anonymous:
            return queryset.filter(published=True)
        return queryset """


class LocationType(DjangoObjectType):
    class Meta:
        model = Location
        interfaces = (relay.Node, )

    """ @classmethod
    def get_queryset(cls, queryset, info):
        if info.context.user.is_anonymous:
            return queryset.filter(published=True)
        return queryset """


class Query:
    user = graphene.List(UserType, id=graphene.Int())
    users = graphene.List(UserType)
    locations = graphene.List(LocationType)
    search_donor = graphene.List(UserType, bloodGroup=graphene.String(
    ), district=graphene.String(), municipality=graphene.String())

    me = graphene.Field(UserType)

    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')
        return User.objects.get(pk=id)

    def resolve_users(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')
        return get_user_model().objects.all()

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')

        return user



    def resolve_locations(self, info, **kwargs):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')

        return Location.objects.all()

    def resolve_search_donor(self, info, **kwargs):
        bloodGroup = kwargs.get('bloodGroup')
        district = kwargs.get('district')
        municipality = kwargs.get('municipality')
        require_date = datetime.date.today() - datetime.timedelta(days=100)
        return User.objects.filter(Q(bloodgroup__icontains=bloodGroup) &
                                   Q(district__icontains=district) &
                                   Q(last_donate_date__lte=require_date) &
                                   Q(municipality__icontains=municipality))


class CreateLocation(graphene.Mutation):
    """ id, district, municipality,"""

    id = graphene.String()
    district = graphene.String()
    municipality = graphene.String()

    class Arguments:
        district = graphene.String()
        municipality = graphene.String()

    def mutate(self, info, district, municipality):
        location = Location(district, municipality)
        location.save()

        return CreateLocation(district=location.district, municipality=location.municipality)




class CreateUser(graphene.Mutation):

    """ id, password, lastLogin, isSuperuser, isStaff, isActive, dateJoined,
    email, address, avatar, firstName, middleName, lastName, phone, bloodgroup,
    lastDonateDate, donationNo"""
    user = graphene.Field(UserType)

    class Arguments:
        """ password = graphene.String()
        lastLogin = graphene.String()
        isSuperuser = graphene.String()
        isStaff = graphene.String()
        isActive = graphene.String()
        avatar = graphene.String()
        dateJoined = graphene.String() """
        email = graphene.String()
        address = graphene.String()
        firstName = graphene.String()
        middleName = graphene.String()
        lastName = graphene.String()
        phone = graphene.Int()
        bloodgroup = graphene.String()
        lastDonateDate = graphene.types.datetime.DateTime()
        donationNo = graphene.Int()

    def mutate(self, info, password, lastLogin, isSuperuser, isStaff, isActive, dateJoined, email, address, avatar, firstName, middleName, lastName, phone, bloodgroup, lastDonateDate, donationNo):
        """ user = get_user_model()(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save() """
        user = get_user_model()(
            password = password,
            lastLogin = lastLogin,
            isSuperuser = isSuperuser,
            isStaff = isStaff,
            isActive = isActive,
            dateJoined = dateJoined,
            email = email,
            address = address,
            avatar = avatar,
            firstName = firstName,
            middleName = middleName,
            lastName = lastName,
            phone = phone,
            bloodgroup = bloodgroup,
            lastDonateDate = lastDonateDate,
            donationNo = donationNo
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)


class Mutation:
    create_location = CreateLocation.Field()
    create_user = CreateUser.Field()


    def resolve_update_user(self, info, **kwargs):
        pass

    def resolve_delete_user(self, info, **kwargs):
        id = kwargs.get('id')
        user = User.objects.delete(id)

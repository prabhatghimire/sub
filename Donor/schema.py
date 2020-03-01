import graphene
from graphene_django.types import DjangoObjectType
from .models import Event, Bloodbank, Feedback
from graphene import relay


class eventType(DjangoObjectType):
    class Meta:
        model = Event
        #fields = ('title', 'anouncedate', 'detail', 'photo', 'organizer', 'location', 'posteddate')
        interfaces = (relay.Node, )


class bloodBankType(DjangoObjectType):
    class Meta:
        model = Bloodbank
        interfaces = (relay.Node, )

    @classmethod
    def get_queryset(cls, queryset, info):
        if info.context.user.is_anonymous:
            return 'you are not login'
        return queryset


class feedbackType(DjangoObjectType):
    class Meta:
        model = Feedback


class Query:
    event = graphene.List(eventType, id=graphene.ID())
    events = graphene.List(eventType)
    bloodbank = graphene.List(bloodBankType, id=graphene.ID())
    bloodbanks = graphene.List(bloodBankType)
    feedback = graphene.List(feedbackType, id=graphene.Int())
    feedbacks = graphene.List(feedbackType)

    def resolve_events(self, info, **kwargs):
        return Event.objects.all()

    def resolve_event(self, info, id, **kwargs):
        return Event.objects.filter(pk=id)

    def resolve_bloodbanks(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Bloodbank.objects.all()

    def resolve_bloodbank(self, info, id, **kwargs):
        # We can easily optimize query count in the resolve method
        return Bloodbank.objects.filter(pk=id)

    def resolve_feedbacks(self, info, **kwargs):
        return Feedback.objects.all()

    def resolve_feedback(self, info, id, **kwargs):
        return Feedback.objects.filter(pk=id)


class CreateEvent(graphene.Mutation):
    """ title, anouncedate, detail, photo, organizer, location, """
    title = graphene.String()
    anouncedate = graphene.types.datetime.DateTime()
    detail = graphene.String()
    #photo = graphene.FileField()
    organizer = graphene.String()
    location = graphene.String()

    # 2
    class Arguments:
        title = graphene.String()
        anouncedate = graphene.types.datetime.DateTime()
        detail = graphene.String()
        #photo = graphene.FileField()
        organizer = graphene.String()
        location = graphene.String()

    # 3
    def mutate(self, info, title, anouncedate, detail, photo, organizer, location):
        event = Event(title, anouncedate, detail, photo, organizer, location)
        event.save()

        return CreateEvent(title=event.title, anouncedate=event.anouncedate, detail=event.detail, photo=event.photo, organizer=event.organizer, location=event.location)


class CreateBloodBank(graphene.Mutation):
    """ name, phone, location, """
    name = graphene.String()
    phone = graphene.String()
    locction = graphene.String()

    # 2
    class Arguments:
        name = graphene.String()
        phone = graphene.String()
        location = graphene.String()

    # 3
    def mutate(self, info, name, phone, location):
        bloodbank = Bloodbank(name, phone, location)
        bloodbank.save()

        return CreateBloodBank(title=bloodbank.name, anouncedate=bloodbank.phone, detail=bloodbank.location)


class CreateFeedBack(graphene.Mutation):
    """ name, email, subject, comment,"""

    name = graphene.String()
    email = graphene.String()
    subject = graphene.String()
    comment = graphene.String()

    # 2
    class Arguments:
        name = graphene.String()
        email = graphene.String()
        subject = graphene.String()
        comment = graphene.String()

    # 3
    def mutate(self, info, name, email, subject,  comment):
        feedback = Feedback(name, email, subject, comment)
        feedback.save()

        return CreateFeedBack(title=feedback.name, anouncedate=feedback.email, detail=feedback.subject, comment=feedback.scomment)


class Mutation(graphene.ObjectType):
    create_event = CreateEvent.Field()
    create_bloodbank = CreateBloodBank.Field()
    create_feedback = CreateFeedBack.Field()

from django.db import models
from django.contrib.auth.models import AbstractUser


STATUS_CHOICES = (
    ('None', 'None'),
    ('Client', 'Client'),
    ('Coach', 'Coach'),
)


class Member(AbstractUser):
    # this should be protected more
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default=STATUS_CHOICES[0][0])
    bio = models.TextField(blank=True, null=True)
    pic = models.FileField(blank=True, null=True)
    link_code = models.CharField(max_length=20)


    def __str__(self):
        return '{} / {}'.format(self.username, self.status)


    def get_spaces(self):
        return self.space_set.all()



    # method for client to join coach
    # just need coach link_code and client link_code

    def client_join_coach(self, coach_link_code):
        pass

    def coach_link_client(self):
        pass

    def get_all_clients(self):
        pass



class Space(models.Model):
    # find useful way of setting a default
    name = models.CharField(max_length=35)
    members = models.ManyToManyField(Member, through='MemberSpace')

    def __str__(self):
        return self.name

    def get_status_members(self):
        nones = []
        clients = []
        coaches = []
        for i in self.memberspace_set.all():
            if i.member.status == 'None':
                nones.append(i)
            elif i.member.status == 'Client':
                clients.append(i)
            elif i.member.status == 'Coach':
                coaches.append(i)
        return {'Coaches': coaches,
                'Clients': clients,
                 'Nones': nones}

    def coaches(self):
        return self.get_status_members()['Coaches']

    def clients(self):
        return self.get_status_members()['Clients']

    def nones(self):
        return self.get_status_members()['Nones']



class MemberSpace(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    space = models.ForeignKey(Space, on_delete=models.CASCADE)

    def __str__(self):
        return self.member.username
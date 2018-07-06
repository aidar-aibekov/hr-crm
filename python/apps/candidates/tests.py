from rest_framework.test import APITestCase

from apps.base_tests import ListTestMixin, GetInstanceTestMixin, UpdateTestMixin
from apps.candidates.models import Candidate
from apps.candidates.serializers import CandidateDetailSerializer
from apps.interviews.serializers import AuxCandidateSerializer


class CandidatesListTest(APITestCase, ListTestMixin):
    model = Candidate
    serializer = AuxCandidateSerializer


class CandidatesDetailTest(APITestCase, GetInstanceTestMixin):
    model = Candidate
    serializer = CandidateDetailSerializer

    fixtures = ['candidates.json', 'departments.json', 'requests.json', 'users.json', 'vacancies.json',
                'interviews.json']

    def setUp(self):
        self.instance = Candidate.objects.get(pk=1)


class CandidateUpdateTestCase(APITestCase, UpdateTestMixin):
    model = Candidate
    serializer = CandidateDetailSerializer

    fixtures = ['candidates.json', 'departments.json', 'requests.json', 'users.json', 'vacancies.json',
                'interviews.json']

    def setUp(self):
        self.instance = Candidate.objects.get(pk=1)
        self.update_data = {
            "first_name": "Almaz",
            "last_name": "Karat"
        }

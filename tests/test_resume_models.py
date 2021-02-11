import pytest

from django.urls import reverse
from mixer.backend.django import mixer


class TestBasicInfo:
    def setup_method(self):
        self.basic_info = mixer.blend("resume.BasicInfo")

    def test_save(self):
        assert len(self.basic_info.info_id) == 32

    def test_resume_url(self):
        assert self.basic_info.info_id in self.basic_info.resume_url

    def test_str(self):
        components = (
            self.basic_info.name,
            self.basic_info.email,
            self.basic_info.info_id,
        )
        assert all(c in str(self.basic_info) for c in components)


class TestSection:
    def setup_method(self):
        self.section = mixer.blend("resume.Section")

    def test_section_class_name(self):
        assert " " not in self.section.section_class_name
        assert type(self.section.section_class_name) is str

    def test_str(self):
        components = (str(self.section.user), self.section.name)
        assert all(c in str(self.section) for c in components)


def test_list_item():
    list_item = mixer.blend("resume.listitem")
    components = (list_item.headline, list_item.year)
    assert all(c in str(list_item) for c in components)


def test_graph_item():
    graph_item = mixer.blend("resume.GraphItem")
    components = (graph_item.category, graph_item.name, str(graph_item.level))
    assert all(c in str(graph_item) for c in components)


class TestSectionContent:
    def setup_method(self):
        self.graph1 = mixer.cycle(4).blend("resume.GraphItem", category="gr1")
        self.graph2 = mixer.cycle(4).blend("resume.GraphItem", category="gr2")
        self.graph3 = mixer.cycle(4).blend("resume.GraphItem", category="gr3")
        self.graph4 = mixer.cycle(4).blend("resume.GraphItem", category="gr4")

        self.section_content = mixer.blend(
            "resume.SectionContent",
            graph_item=(
                *self.graph1,
                *self.graph2,
                *self.graph3,
                *self.graph4,
            ),
        )

    def test_get_graph_grouped(self):
        graph_grouped = self.section_content.get_graph_grouped()
        assert len(graph_grouped) == 2

    def test_str(self):
        assert self.section_content.name in str(self.section_content)


def test_github_button():
    gh_button = mixer.blend("resume.GitHubButton")
    components = (
        gh_button.user.name,
        gh_button.url,
    )
    assert all(c in str(gh_button) for c in components)

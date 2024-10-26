from github.GithubObject import (Attribute, CompletableGithubObject, NotSet,
                                 Opt, _NotSetType, is_defined, is_optional,
                                 is_optional_list, is_undefined)
from github.PaginatedList import PaginatedList
from github.PullRequest import PullRequest
from github.PullRequestComment import PullRequestComment


def get_pulls(
    self,
    state: Opt[str] = NotSet,
    sort: Opt[str] = NotSet,
    direction: Opt[str] = NotSet,
    base: Opt[str] = NotSet,
    head: Opt[str] = NotSet,
    extra: dict = {}
) -> PaginatedList[PullRequest]:
    """
    :calls: `GET /repos/{owner}/{repo}/pulls <https://docs.github.com/en/rest/reference/pulls>`_
    :param state: string
    :param sort: string
    :param direction: string
    :param base: string
    :param head: string
    :rtype: :class:`PaginatedList` of :class:`github.PullRequest.PullRequest`
    """
    assert is_optional(state, str), state
    assert is_optional(sort, str), sort
    assert is_optional(direction, str), direction
    assert is_optional(base, str), base
    assert is_optional(head, str), head
    url_parameters = dict()
    if is_defined(state):
        url_parameters["state"] = state
    if is_defined(sort):
        url_parameters["sort"] = sort
    if is_defined(direction):
        url_parameters["direction"] = direction
    if is_defined(base):
        url_parameters["base"] = base
    if is_defined(head):
        url_parameters["head"] = head
    
    url_parameters.update(extra)
    
    return PaginatedList(
        PullRequest,
        self._requester,
        f"{self.url}/pulls",
        url_parameters,
    )
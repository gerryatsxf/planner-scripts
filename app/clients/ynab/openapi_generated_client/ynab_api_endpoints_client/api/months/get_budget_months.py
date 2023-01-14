from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.month_summaries_response import MonthSummariesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    budget_id: str,
    *,
    client: Client,
    last_knowledge_of_server: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/budgets/{budget_id}/months".format(client.base_url, budget_id=budget_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["last_knowledge_of_server"] = last_knowledge_of_server

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[ErrorResponse, MonthSummariesResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = MonthSummariesResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[ErrorResponse, MonthSummariesResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    budget_id: str,
    *,
    client: Client,
    last_knowledge_of_server: Union[Unset, None, int] = UNSET,
) -> Response[Union[ErrorResponse, MonthSummariesResponse]]:
    """List budget months

     Returns all budget months

    Args:
        budget_id (str):
        last_knowledge_of_server (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, MonthSummariesResponse]]
    """

    kwargs = _get_kwargs(
        budget_id=budget_id,
        client=client,
        last_knowledge_of_server=last_knowledge_of_server,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    budget_id: str,
    *,
    client: Client,
    last_knowledge_of_server: Union[Unset, None, int] = UNSET,
) -> Optional[Union[ErrorResponse, MonthSummariesResponse]]:
    """List budget months

     Returns all budget months

    Args:
        budget_id (str):
        last_knowledge_of_server (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, MonthSummariesResponse]]
    """

    return sync_detailed(
        budget_id=budget_id,
        client=client,
        last_knowledge_of_server=last_knowledge_of_server,
    ).parsed


async def asyncio_detailed(
    budget_id: str,
    *,
    client: Client,
    last_knowledge_of_server: Union[Unset, None, int] = UNSET,
) -> Response[Union[ErrorResponse, MonthSummariesResponse]]:
    """List budget months

     Returns all budget months

    Args:
        budget_id (str):
        last_knowledge_of_server (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, MonthSummariesResponse]]
    """

    kwargs = _get_kwargs(
        budget_id=budget_id,
        client=client,
        last_knowledge_of_server=last_knowledge_of_server,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    budget_id: str,
    *,
    client: Client,
    last_knowledge_of_server: Union[Unset, None, int] = UNSET,
) -> Optional[Union[ErrorResponse, MonthSummariesResponse]]:
    """List budget months

     Returns all budget months

    Args:
        budget_id (str):
        last_knowledge_of_server (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, MonthSummariesResponse]]
    """

    return (
        await asyncio_detailed(
            budget_id=budget_id,
            client=client,
            last_knowledge_of_server=last_knowledge_of_server,
        )
    ).parsed

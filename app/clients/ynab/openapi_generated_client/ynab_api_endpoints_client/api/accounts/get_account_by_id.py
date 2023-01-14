from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.account_response import AccountResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    budget_id: str,
    account_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/budgets/{budget_id}/accounts/{account_id}".format(
        client.base_url, budget_id=budget_id, account_id=account_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[AccountResponse, ErrorResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AccountResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[AccountResponse, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    budget_id: str,
    account_id: str,
    *,
    client: Client,
) -> Response[Union[AccountResponse, ErrorResponse]]:
    """Single account

     Returns a single account

    Args:
        budget_id (str):
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AccountResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        budget_id=budget_id,
        account_id=account_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    budget_id: str,
    account_id: str,
    *,
    client: Client,
) -> Optional[Union[AccountResponse, ErrorResponse]]:
    """Single account

     Returns a single account

    Args:
        budget_id (str):
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AccountResponse, ErrorResponse]]
    """

    return sync_detailed(
        budget_id=budget_id,
        account_id=account_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    budget_id: str,
    account_id: str,
    *,
    client: Client,
) -> Response[Union[AccountResponse, ErrorResponse]]:
    """Single account

     Returns a single account

    Args:
        budget_id (str):
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AccountResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        budget_id=budget_id,
        account_id=account_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    budget_id: str,
    account_id: str,
    *,
    client: Client,
) -> Optional[Union[AccountResponse, ErrorResponse]]:
    """Single account

     Returns a single account

    Args:
        budget_id (str):
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AccountResponse, ErrorResponse]]
    """

    return (
        await asyncio_detailed(
            budget_id=budget_id,
            account_id=account_id,
            client=client,
        )
    ).parsed

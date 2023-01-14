from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.payee_locations_response import PayeeLocationsResponse
from ...types import Response


def _get_kwargs(
    budget_id: str,
    payee_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/budgets/{budget_id}/payees/{payee_id}/payee_locations".format(
        client.base_url, budget_id=budget_id, payee_id=payee_id
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


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[ErrorResponse, PayeeLocationsResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PayeeLocationsResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, PayeeLocationsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    budget_id: str,
    payee_id: str,
    *,
    client: Client,
) -> Response[Union[ErrorResponse, PayeeLocationsResponse]]:
    """List locations for a payee

     Returns all payee locations for a specified payee

    Args:
        budget_id (str):
        payee_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PayeeLocationsResponse]]
    """

    kwargs = _get_kwargs(
        budget_id=budget_id,
        payee_id=payee_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    budget_id: str,
    payee_id: str,
    *,
    client: Client,
) -> Optional[Union[ErrorResponse, PayeeLocationsResponse]]:
    """List locations for a payee

     Returns all payee locations for a specified payee

    Args:
        budget_id (str):
        payee_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PayeeLocationsResponse]]
    """

    return sync_detailed(
        budget_id=budget_id,
        payee_id=payee_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    budget_id: str,
    payee_id: str,
    *,
    client: Client,
) -> Response[Union[ErrorResponse, PayeeLocationsResponse]]:
    """List locations for a payee

     Returns all payee locations for a specified payee

    Args:
        budget_id (str):
        payee_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PayeeLocationsResponse]]
    """

    kwargs = _get_kwargs(
        budget_id=budget_id,
        payee_id=payee_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    budget_id: str,
    payee_id: str,
    *,
    client: Client,
) -> Optional[Union[ErrorResponse, PayeeLocationsResponse]]:
    """List locations for a payee

     Returns all payee locations for a specified payee

    Args:
        budget_id (str):
        payee_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PayeeLocationsResponse]]
    """

    return (
        await asyncio_detailed(
            budget_id=budget_id,
            payee_id=payee_id,
            client=client,
        )
    ).parsed

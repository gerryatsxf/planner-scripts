from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.transactions_import_response import TransactionsImportResponse
from ...types import Response


def _get_kwargs(
    budget_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/budgets/{budget_id}/transactions/import".format(client.base_url, budget_id=budget_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[ErrorResponse, TransactionsImportResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TransactionsImportResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.CREATED:
        response_201 = TransactionsImportResponse.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[ErrorResponse, TransactionsImportResponse]]:
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
) -> Response[Union[ErrorResponse, TransactionsImportResponse]]:
    """Import transactions

     Imports available transactions on all linked accounts for the given budget.  Linked accounts allow
    transactions to be imported directly from a specified financial institution and this endpoint
    initiates that import.  Sending a request to this endpoint is the equivalent of clicking \"Import\"
    on each account in the web application or tapping the \"New Transactions\" banner in the mobile
    applications.  The response for this endpoint contains the transaction ids that have been imported.

    Args:
        budget_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, TransactionsImportResponse]]
    """

    kwargs = _get_kwargs(
        budget_id=budget_id,
        client=client,
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
) -> Optional[Union[ErrorResponse, TransactionsImportResponse]]:
    """Import transactions

     Imports available transactions on all linked accounts for the given budget.  Linked accounts allow
    transactions to be imported directly from a specified financial institution and this endpoint
    initiates that import.  Sending a request to this endpoint is the equivalent of clicking \"Import\"
    on each account in the web application or tapping the \"New Transactions\" banner in the mobile
    applications.  The response for this endpoint contains the transaction ids that have been imported.

    Args:
        budget_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, TransactionsImportResponse]]
    """

    return sync_detailed(
        budget_id=budget_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    budget_id: str,
    *,
    client: Client,
) -> Response[Union[ErrorResponse, TransactionsImportResponse]]:
    """Import transactions

     Imports available transactions on all linked accounts for the given budget.  Linked accounts allow
    transactions to be imported directly from a specified financial institution and this endpoint
    initiates that import.  Sending a request to this endpoint is the equivalent of clicking \"Import\"
    on each account in the web application or tapping the \"New Transactions\" banner in the mobile
    applications.  The response for this endpoint contains the transaction ids that have been imported.

    Args:
        budget_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, TransactionsImportResponse]]
    """

    kwargs = _get_kwargs(
        budget_id=budget_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    budget_id: str,
    *,
    client: Client,
) -> Optional[Union[ErrorResponse, TransactionsImportResponse]]:
    """Import transactions

     Imports available transactions on all linked accounts for the given budget.  Linked accounts allow
    transactions to be imported directly from a specified financial institution and this endpoint
    initiates that import.  Sending a request to this endpoint is the equivalent of clicking \"Import\"
    on each account in the web application or tapping the \"New Transactions\" banner in the mobile
    applications.  The response for this endpoint contains the transaction ids that have been imported.

    Args:
        budget_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, TransactionsImportResponse]]
    """

    return (
        await asyncio_detailed(
            budget_id=budget_id,
            client=client,
        )
    ).parsed

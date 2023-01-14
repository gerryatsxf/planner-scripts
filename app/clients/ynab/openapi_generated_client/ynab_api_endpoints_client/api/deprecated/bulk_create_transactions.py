from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.bulk_response import BulkResponse
from ...models.bulk_transactions import BulkTransactions
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    budget_id: str,
    *,
    client: Client,
    json_body: BulkTransactions,
) -> Dict[str, Any]:
    url = "{}/budgets/{budget_id}/transactions/bulk".format(client.base_url, budget_id=budget_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[BulkResponse, ErrorResponse]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = BulkResponse.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[BulkResponse, ErrorResponse]]:
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
    json_body: BulkTransactions,
) -> Response[Union[BulkResponse, ErrorResponse]]:
    """Bulk create transactions

     Creates multiple transactions.  Although this endpoint is still supported, it is recommended to use
    'POST /budgets/{budget_id}/transactions' to create multiple transactions.

    Args:
        budget_id (str):
        json_body (BulkTransactions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BulkResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        budget_id=budget_id,
        client=client,
        json_body=json_body,
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
    json_body: BulkTransactions,
) -> Optional[Union[BulkResponse, ErrorResponse]]:
    """Bulk create transactions

     Creates multiple transactions.  Although this endpoint is still supported, it is recommended to use
    'POST /budgets/{budget_id}/transactions' to create multiple transactions.

    Args:
        budget_id (str):
        json_body (BulkTransactions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BulkResponse, ErrorResponse]]
    """

    return sync_detailed(
        budget_id=budget_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    budget_id: str,
    *,
    client: Client,
    json_body: BulkTransactions,
) -> Response[Union[BulkResponse, ErrorResponse]]:
    """Bulk create transactions

     Creates multiple transactions.  Although this endpoint is still supported, it is recommended to use
    'POST /budgets/{budget_id}/transactions' to create multiple transactions.

    Args:
        budget_id (str):
        json_body (BulkTransactions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BulkResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        budget_id=budget_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    budget_id: str,
    *,
    client: Client,
    json_body: BulkTransactions,
) -> Optional[Union[BulkResponse, ErrorResponse]]:
    """Bulk create transactions

     Creates multiple transactions.  Although this endpoint is still supported, it is recommended to use
    'POST /budgets/{budget_id}/transactions' to create multiple transactions.

    Args:
        budget_id (str):
        json_body (BulkTransactions):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BulkResponse, ErrorResponse]]
    """

    return (
        await asyncio_detailed(
            budget_id=budget_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.save_category_response import SaveCategoryResponse
from ...models.save_month_category_wrapper import SaveMonthCategoryWrapper
from ...types import Response


def _get_kwargs(
    budget_id: str,
    month: datetime.date,
    category_id: str,
    *,
    client: Client,
    json_body: SaveMonthCategoryWrapper,
) -> Dict[str, Any]:
    url = "{}/budgets/{budget_id}/months/{month}/categories/{category_id}".format(
        client.base_url, budget_id=budget_id, month=month, category_id=category_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[ErrorResponse, SaveCategoryResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SaveCategoryResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[ErrorResponse, SaveCategoryResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    budget_id: str,
    month: datetime.date,
    category_id: str,
    *,
    client: Client,
    json_body: SaveMonthCategoryWrapper,
) -> Response[Union[ErrorResponse, SaveCategoryResponse]]:
    """Update a category for a specific month

     Update a category for a specific month.  Only `budgeted` amount can be updated.

    Args:
        budget_id (str):
        month (datetime.date):
        category_id (str):
        json_body (SaveMonthCategoryWrapper):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SaveCategoryResponse]]
    """

    kwargs = _get_kwargs(
        budget_id=budget_id,
        month=month,
        category_id=category_id,
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
    month: datetime.date,
    category_id: str,
    *,
    client: Client,
    json_body: SaveMonthCategoryWrapper,
) -> Optional[Union[ErrorResponse, SaveCategoryResponse]]:
    """Update a category for a specific month

     Update a category for a specific month.  Only `budgeted` amount can be updated.

    Args:
        budget_id (str):
        month (datetime.date):
        category_id (str):
        json_body (SaveMonthCategoryWrapper):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SaveCategoryResponse]]
    """

    return sync_detailed(
        budget_id=budget_id,
        month=month,
        category_id=category_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    budget_id: str,
    month: datetime.date,
    category_id: str,
    *,
    client: Client,
    json_body: SaveMonthCategoryWrapper,
) -> Response[Union[ErrorResponse, SaveCategoryResponse]]:
    """Update a category for a specific month

     Update a category for a specific month.  Only `budgeted` amount can be updated.

    Args:
        budget_id (str):
        month (datetime.date):
        category_id (str):
        json_body (SaveMonthCategoryWrapper):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SaveCategoryResponse]]
    """

    kwargs = _get_kwargs(
        budget_id=budget_id,
        month=month,
        category_id=category_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    budget_id: str,
    month: datetime.date,
    category_id: str,
    *,
    client: Client,
    json_body: SaveMonthCategoryWrapper,
) -> Optional[Union[ErrorResponse, SaveCategoryResponse]]:
    """Update a category for a specific month

     Update a category for a specific month.  Only `budgeted` amount can be updated.

    Args:
        budget_id (str):
        month (datetime.date):
        category_id (str):
        json_body (SaveMonthCategoryWrapper):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SaveCategoryResponse]]
    """

    return (
        await asyncio_detailed(
            budget_id=budget_id,
            month=month,
            category_id=category_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

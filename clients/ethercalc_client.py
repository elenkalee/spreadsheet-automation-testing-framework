from typing import Any

import requests

from clients.api_client import APIClient


class EtherCalcClient(APIClient):
    def create_page(
        self,
        sheet_id: str | None = None,
        snapshot: str = "",
    ) -> requests.Response:
        payload = {"snapshot": snapshot}
        if sheet_id is not None:
            payload["room"] = sheet_id

        return self.post("_", json=payload)

    def get_page_content(self, sheet_id: str) -> str:
        response = self.get(f"_/{sheet_id}")
        response.raise_for_status()
        return response.text

    def get_cells(self, sheet_id: str) -> dict[str, Any]:
        response = self.get(f"_/{sheet_id}/cells")
        response.raise_for_status()
        return response.json()

    def get_cell(self, sheet_id: str, cell: str) -> dict[str, Any]:
        response = self.get(f"_/{sheet_id}/cells/{cell}")
        response.raise_for_status()
        return response.json()

    def export_csv(self, sheet_id: str) -> str:
        response = self.get(f"{sheet_id}.csv")
        response.raise_for_status()
        return response.text

    def export_json(self, sheet_id: str) -> list[list[Any]]:
        response = self.get(f"{sheet_id}.csv.json")
        response.raise_for_status()
        return response.json()

    def export_html(self, sheet_id: str) -> str:
        response = self.get(f"{sheet_id}.html")
        response.raise_for_status()
        return response.text

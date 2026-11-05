import test from "node:test";
import assert from "node:assert/strict";
import { routeFor } from "@desk/routes";

test("routes tagged parcels to express", () => {
  assert.equal(routeFor("X-41"), "express");
});

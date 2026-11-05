export function routeFor(label) {
  return label?.startsWith("X-") ? "express" : "standard";
}
